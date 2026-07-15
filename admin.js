// ── PIN ───────────────────────────────────────────────────────────────────────
let pin = '';
function pk(k) {
  if (pin.length >= 6) return;
  pin += k; dots();
  if (pin.length === 4) { const s = getStaffByPin(pin); if (s) { doLogin(s); return; } }
  if (pin.length === 6) tryLogin();
}
function pdel() { pin = pin.slice(0,-1); dots(); }
function dots(err) {
  for (let i=0;i<4;i++) {
    const d = document.getElementById('d'+i);
    d.className = 'pin-dot'+(i<pin.length?' filled':'')+(err?' error':'');
  }
}
function tryLogin() {
  const s = getStaffByPin(pin);
  if (s) { doLogin(s); }
  else {
    dots(true);
    document.getElementById('loginErr').textContent = 'Неверный PIN';
    pin = '';
    setTimeout(()=>{ dots(); document.getElementById('loginErr').textContent=''; }, 1200);
  }
}

// ── SESSION ───────────────────────────────────────────────────────────────────
let ME = null;
let TAB = 'queue';

function doLogin(staff) {
  ME = staff; TAB = 'queue';
  document.getElementById('loginScreen').style.display = 'none';
  document.getElementById('adminScreen').style.display = 'block';
  document.getElementById('aName').textContent = staff.name;
  document.getElementById('aCab').textContent  = 'Кабинет ' + staff.cabinet + ' · ' + staff.floor;
  renderAll();
  startRefresh();
}
function logout() {
  ME = null; pin = ''; dots(); stopRefresh();
  document.getElementById('adminScreen').style.display = 'none';
  document.getElementById('loginScreen').style.display = 'flex';
}

// ── STORAGE ───────────────────────────────────────────────────────────────────
let CACHE_QUEUE  = {};
let CACHE_ACTIVE = {};

function getQueueData() {
  if (!ME) return { current:0, queue:[], history:[] };
  const d = CACHE_QUEUE[ME.id];
  if (!d) return { current:0, queue:[], history:[] };
  if (!d.queue)   d.queue   = [];
  if (!d.history) d.history = [];
  return d;
}

function getMyActive() {
  if (!ME) return [];
  const active = CACHE_ACTIVE[ME.id];
  return Array.isArray(active) ? active : [];
}

function setMyActive(arr) {
  if (!ME) return;
  CACHE_ACTIVE[ME.id] = arr;
  window.db.ref('active/' + ME.id).set(arr);
}

function saveQueueData(d) {
  CACHE_QUEUE[ME.id] = d;
  window.db.ref('queues/' + ME.id).set(d);
}

function listenFirebase() {
  window.db.ref('active').on('value', function(snap) {
    CACHE_ACTIVE = snap.val() || {};
    if (ME) renderAll();
  });
  window.db.ref('queues').on('value', function(snap) {
    CACHE_QUEUE = snap.val() || {};
    if (ME) renderAll();
  });
}

// ── RENDER ALL ────────────────────────────────────────────────────────────────
function renderAll() { renderTabs(); TAB === 'queue' ? renderQueue() : renderSubjects(); }

function renderTabs() {
  const data    = getQueueData();
  const waiting = data.queue.filter(q => !q.called).length;
  const active  = getMyActive().length;
  document.getElementById('aTabs').innerHTML =
    '<button class="a-tab '+(TAB==='queue'?'on':'')+'" onclick="switchTab(\'queue\')">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>' +
      'Очередь' +
      (waiting > 0 ? '<span class="a-tbadge o">'+waiting+'</span>' : '') +
    '</button>' +
    '<button class="a-tab '+(TAB==='subjects'?'on':'')+'" onclick="switchTab(\'subjects\')">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>' +
      'Мой стол' +
      (active > 0 ? '<span class="a-tbadge g">ON</span>' : '<span class="a-tbadge">OFF</span>') +
    '</button>';
}
function switchTab(t) { TAB = t; renderAll(); }

// ── QUEUE TAB ─────────────────────────────────────────────────────────────────
function renderQueue() {
  const data    = getQueueData();
  const waiting = data.queue.filter(q => !q.called);
  const served  = data.history.length;
  const pfx     = ME.id.replace('staff_','S');

  const curHTML = data.current
    ? '<div class="cur-num"><span class="cur-pfx">'+pfx+'-</span>'+String(data.current).padStart(3,'0')+'</div>'
    : '<div class="cur-empty">Ожидание...</div>';

  const nxt = waiting[0];
  const nextCard = nxt
    ? '<div class="next-card">' +
        '<div class="nc-row"><div class="nc-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>' +
          '<div><div class="nc-v">'+pfx+'-'+String(nxt.number).padStart(3,'0')+'</div><div class="nc-l">Следующий</div></div></div>' +
        '<div class="nc-row"><div class="nc-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>' +
          '<div><div class="nc-v">'+nxt.time+'</div><div class="nc-l">Время</div></div></div>' +
      '</div>'
    : '';

  const qItems = waiting.length
    ? waiting.slice(0,15).map(function(q,i) {
        return '<div class="q-row '+(i===0?'nx':'')+'">' +
          '<div class="q-n '+(i===0?'nx':'')+'">'+String(q.number).padStart(3,'0')+'</div>' +
          '<div class="q-b"><div class="q-c">'+q.time+'</div>' +
          '<div class="q-nm">'+(q.name||'—')+'</div></div>' +
          (i===0 ? '<span class="nx-tag">Следующий</span>' : '') +
          '<button class="q-del" title="Удалить талон" onclick="deleteTicket('+q.number+')">✕</button>' +
        '</div>';
      }).join('')
    : '<div class="empty-q"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg><p>Очередь пуста</p></div>';

  const hist = data.history.length
    ? data.history.slice().reverse().slice(0,8).map(function(h) {
        return '<div class="q-row">' +
          '<div class="q-n" style="background:#e8ecf8;color:var(--text-3)">'+String(h.number).padStart(3,'0')+'</div>' +
          '<div class="q-b"><div class="q-c">'+h.calledAt+'</div><div class="q-nm">'+(h.name||'—')+'</div></div>' +
        '</div>';
      }).join('')
    : '<p style="color:var(--text-3);font-size:12px;padding:6px 0">Нет записей</p>';

  const myAct = getMyActive();
  const warnHTML = myAct.length === 0
    ? '<div class="warn-box"><span>⚠️</span><div><b>Стол не активен</b><br>Перейдите в «Мой стол» и активируйте приём</div></div>'
    : '';

  document.getElementById('aContent').innerHTML =
    warnHTML +
    '<div class="stats">' +
      '<div class="sc"><div class="sv">'+(data.current||'—')+'</div><div class="sl">Вызван</div></div>' +
      '<div class="sc o"><div class="sv">'+waiting.length+'</div><div class="sl">Ожидают</div></div>' +
      '<div class="sc g"><div class="sv">'+served+'</div><div class="sl">Обслужено</div></div>' +
    '</div>' +
    '<div class="panel">' +
      '<div class="p-top">' +
        '<div class="p-top-l"><div class="p-sub">'+ME.cabinet+' · '+ME.floor+'</div><div class="p-title">'+ME.name+'</div></div>' +
        '<div class="p-badge">'+waiting.length+' ожидают</div>' +
      '</div>' +
      '<div class="cur-block"><div><div class="cur-lbl">Текущий вызов</div>'+curHTML+'</div>'+nextCard+'</div>' +
      '<div class="acts">' +
        '<button class="btn-next" onclick="callNext()" '+(waiting.length===0?'disabled':'')+'>'+
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>'+
          'Следующий'+(waiting.length>0?' · '+waiting.length+' чел.':'')+
        '</button>' +
        '<button class="btn-recall" onclick="recallCurrent()" '+(data.current?'':'disabled')+'>'+
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.07 1.18 2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>'+
          'Қайта / Повтор'+
        '</button>' +
        '<button class="btn-rst" onclick="resetQ()">'+
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 102.13-9.36L1 10"/></svg>Сброс'+
        '</button>' +
      '</div>' +
      '<hr class="dash"><div class="ls"><div class="ls-h"><span class="ls-t">В очереди</span><span class="ls-b">'+waiting.length+'</span></div><div class="q-list">'+qItems+'</div></div>' +
      '<hr class="dash"><div class="ls"><div class="ls-h"><span class="ls-t">История</span><span class="ls-b g">'+served+'</span></div><div class="q-list">'+hist+'</div></div>' +
    '</div>';
}

// ── SUBJECTS TAB (replaces Programs tab) ─────────────────────────────────────
function renderSubjects() {
  if (!ME) return;
  const myAct  = getMyActive();
  const isOn   = myAct.length > 0;
  const subjects = ME.subjects || [];

  // Display subject list
  const subjRows = subjects.map(function(s) {
    // Skip internal markers for display
    const display = s.startsWith('__') ? markerLabel(s) : s;
    return '<div class="prog-item">' +
      '<span class="prog-code" style="min-width:auto;font-size:12px;color:var(--text-2)">📋</span>' +
      '<span class="prog-name">'+display+'</span>' +
    '</div>';
  }).join('');

  document.getElementById('aContent').innerHTML =
    '<div class="progs-header">' +
      '<div><h3>Мой стол: '+ME.cabinet+'</h3><p>'+ME.floor+' · Управление активностью</p></div>' +
      '<div class="progs-counts">' +
        '<div class="pc '+(isOn?'g':'')+'"><div class="pc-v">'+(isOn?'ВКЛ':'ВЫКЛ')+'</div><div class="pc-l">Статус</div></div>' +
      '</div>' +
    '</div>' +

    // Big ON/OFF toggle
    '<div class="panel" style="margin-bottom:14px">' +
      '<div style="padding:24px 20px;text-align:center">' +
        '<div style="font-size:13px;color:var(--text-2);margin-bottom:16px">Включите приём, чтобы студенты могли получить талон к вашему столу</div>' +
        '<div style="display:flex;gap:12px;justify-content:center">' +
          '<button class="btn-all-on" onclick="deskOn()" style="padding:14px 28px;font-size:14px">✓ Открыть приём</button>' +
          '<button class="btn-all-off" onclick="deskOff()" style="padding:14px 28px;font-size:14px">✕ Закрыть приём</button>' +
        '</div>' +
        '<div style="margin-top:16px;padding:12px 16px;background:'+(isOn?'#f0fdf4':'#fff8e6')+';border-radius:12px;border:1.5px solid '+(isOn?'#bbf7d0':'#ffd970')+';font-size:13px;font-weight:700;color:'+(isOn?'#059669':'#7a5a00')+'">' +
          (isOn ? '🟢 Приём открыт — студенты видят ваш стол' : '🟡 Приём закрыт — студенты не видят ваш стол') +
        '</div>' +
      '</div>' +
    '</div>' +

    // Subject list (informational)
    (subjects.length > 0
      ? '<div class="level-panel">' +
          '<div class="lp-head"><div class="lp-title">Мои направления</div></div>' +
          '<div class="prog-items">'+subjRows+'</div>' +
        '</div>'
      : '') ;
}

function markerLabel(marker) {
  const map = {
    '__TIPO__':     'ТиПО (после колледжа)',
    '__VO__':       'ВО (после высшего образования)',
    '__MASTER__':   'Магистратура / Докторантура',
    '__COLLEGE__':  'Высший колледж',
    '__CREATIVE__': 'Творческий ОП',
  };
  return map[marker] || marker;
}

// Desk ON/OFF — simple: when ON we push a sentinel value so Firebase knows it's active
function deskOn() {
  // Store desk marker as active
  setMyActive(ME.subjects || ['__ACTIVE__']);
  renderAll();
  toast('✅ Приём открыт — ' + ME.cabinet);
}
function deskOff() {
  setMyActive([]);
  renderAll();
  toast('⛔ Приём закрыт — ' + ME.cabinet);
}

// ── QUEUE ACTIONS ─────────────────────────────────────────────────────────────
function callNext() {
  const data = getQueueData();
  const w = data.queue.filter(q => !q.called);
  if (!w.length) return;
  const nxt = w[0];
  nxt.called   = true;
  data.current = nxt.number;
  data.history.push({ number:nxt.number, code:nxt.code, name:nxt.name, calledAt:nowT() });
  saveQueueData(data);
  renderAll();
  toast('▶ ' + ME.id.replace('staff_','S') + '-' + String(nxt.number).padStart(3,'0') + ' — ' + (nxt.name||'').substring(0,28));
}

function recallCurrent() {
  const data = getQueueData();
  if (!data.current) return;
  const pfx = ME.id.replace('staff_','S');
  const numStr = pfx + '-' + String(data.current).padStart(3,'0');
  window.db.ref('queues/' + ME.id + '/current').set(0, function() {
    setTimeout(function() {
      window.db.ref('queues/' + ME.id + '/current').set(data.current);
    }, 400);
  });
  toast('🔔 Қайта шақырылды / Повторный вызов: ' + numStr);
}

function deleteTicket(number) {
  const data = getQueueData();
  const t = data.queue.find(function(q){ return q.number === number && !q.called; });
  if (!t) return;
  const pfx = ME.id.replace('staff_','S');
  const numStr = pfx + '-' + String(number).padStart(3,'0');
  if (!confirm('Удалить талон ' + numStr + ' (' + (t.name||'—') + ') из очереди?')) return;
  data.queue = data.queue.filter(function(q){ return !(q.number === number && !q.called); });
  saveQueueData(data);
  renderAll();
  toast('🗑 Талон ' + numStr + ' удалён');
}

function resetQ() {
  if (!confirm('Сбросить очередь?')) return;
  saveQueueData({ current:0, queue:[], history:[] });
  if (window.db) window.db.ref('meta/globalCounter').set(0);
  renderAll();
  toast('Очередь сброшена');
}

// ── HELPERS ───────────────────────────────────────────────────────────────────
function nowT() { return new Date().toLocaleTimeString('ru-RU',{hour:'2-digit',minute:'2-digit'}); }
function toast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2800);
}
let timer = null;
function startRefresh() { timer = setInterval(function(){ if(ME) renderAll(); }, 3500); }
function stopRefresh()  { if(timer) clearInterval(timer); }

// ── AUTO DAILY RESET ──────────────────────────────────────────────────────────
function todayStr() { return new Date().toISOString().slice(0,10); }

function doAutoReset() {
  if (!window.db) return;
  window.db.ref('queues').once('value', function(snap) {
    const all = snap.val() || {};
    const updates = {};
    Object.keys(all).forEach(function(id) {
      updates[id] = { current:0, queue:[], history:[] };
    });
    window.db.ref('queues').set(updates);
  });
  window.db.ref('active').set({});
  window.db.ref('meta/globalCounter').set(0);
  window.db.ref('meta/lastResetDate').set(todayStr());
  toast('🔄 Жаңа күн — деректер тазартылды');
}

function checkDailyReset() {
  if (!window.db) return;
  window.db.ref('meta/lastResetDate').once('value', function(snap) {
    const last = snap.val();
    const today = todayStr();
    if (last && last !== today) { doAutoReset(); }
    else if (!last) { window.db.ref('meta/lastResetDate').set(today); }
  });
}

checkDailyReset();
listenFirebase();
