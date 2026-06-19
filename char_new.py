NEW_CHAR = r"""// ── CHARACTER ─────────────────────────────────────────────────────────────────
function renderCharacter(state) {
  const greet = { rus:'Добро пожаловать! 👋', kaz:'Қош келдіңіз! 👋', eng:'Welcome! 👋' };
  const think  = { rus:'Хм, что выбрать?', kaz:'Не таңдасам?', eng:'What to choose?' };
  const wait   = { rus:'Жду своей очереди...', kaz:'Кезегімді күтемін...', eng:'Waiting my turn...' };

  const defs = `<defs>
    <radialGradient id="gFace" cx="42%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#FFE2CC"/><stop offset="55%" stop-color="#F4C5A0"/><stop offset="100%" stop-color="#D08860"/>
    </radialGradient>
    <radialGradient id="gEar" cx="40%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#F4C5A0"/><stop offset="100%" stop-color="#D09060"/>
    </radialGradient>
    <linearGradient id="gHairT" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#A86028"/><stop offset="40%" stop-color="#6B3A18"/><stop offset="100%" stop-color="#2A1000"/>
    </linearGradient>
    <linearGradient id="gHairS" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#7A4820"/><stop offset="100%" stop-color="#2A1000"/>
    </linearGradient>
    <linearGradient id="gJacket" x1="10%" y1="0%" x2="90%" y2="100%">
      <stop offset="0%" stop-color="#4AAC58"/><stop offset="50%" stop-color="#2E7A3A"/><stop offset="100%" stop-color="#184A20"/>
    </linearGradient>
    <linearGradient id="gJacketL" x1="0%" y1="10%" x2="100%" y2="90%">
      <stop offset="0%" stop-color="#3A9848"/><stop offset="100%" stop-color="#164820"/>
    </linearGradient>
    <linearGradient id="gJacketR" x1="100%" y1="10%" x2="0%" y2="90%">
      <stop offset="0%" stop-color="#3A9848"/><stop offset="100%" stop-color="#164820"/>
    </linearGradient>
    <linearGradient id="gPants" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#D8B855"/><stop offset="55%" stop-color="#C4A038"/><stop offset="100%" stop-color="#907018"/>
    </linearGradient>
    <linearGradient id="gBag" x1="10%" y1="5%" x2="90%" y2="95%">
      <stop offset="0%" stop-color="#2E3E72"/><stop offset="100%" stop-color="#0A1430"/>
    </linearGradient>
    <linearGradient id="gShoeL" x1="0%" y1="0%" x2="60%" y2="100%">
      <stop offset="0%" stop-color="#EE4444"/><stop offset="100%" stop-color="#881818"/>
    </linearGradient>
    <linearGradient id="gShoeR" x1="100%" y1="0%" x2="40%" y2="100%">
      <stop offset="0%" stop-color="#EE4444"/><stop offset="100%" stop-color="#881818"/>
    </linearGradient>
    <radialGradient id="gEye" cx="35%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#6A8ED0"/><stop offset="100%" stop-color="#284888"/>
    </radialGradient>
    <filter id="fShadow"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="rgba(0,0,0,.2)"/></filter>
    <filter id="fSoft"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(0,0,0,.15)"/></filter>
  </defs>`;

  const svg = `<svg viewBox="0 0 300 430" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:240px;height:344px;display:block">
    ${defs}

    <!-- ground shadow -->
    <ellipse cx="150" cy="422" rx="72" ry="11" fill="rgba(48,86,211,.16)"/>

    <!-- ══ RED CONVERSE SHOES ══ -->
    <!-- Left shoe -->
    <path d="M74 404 Q68 386 82 374 Q96 366 112 370 Q124 374 126 388 Q128 402 118 408 Q100 414 74 404Z" fill="url(#gShoeL)"/>
    <path d="M72 404 Q68 410 82 416 Q102 420 124 410 Q130 406 128 400 Q126 408 116 412 Q98 416 72 404Z" fill="#DCDCD0"/>
    <rect x="90" y="372" width="26" height="28" rx="3" fill="rgba(255,255,255,.13)"/>
    <line x1="91" y1="376" x2="115" y2="376" stroke="rgba(255,255,255,.6)" stroke-width="1.5" stroke-linecap="round"/>
    <line x1="91" y1="381" x2="115" y2="381" stroke="rgba(255,255,255,.5)" stroke-width="1.5" stroke-linecap="round"/>
    <line x1="91" y1="386" x2="115" y2="386" stroke="rgba(255,255,255,.45)" stroke-width="1.5" stroke-linecap="round"/>
    <ellipse cx="84" cy="404" rx="13" ry="5.5" fill="rgba(255,255,255,.32)"/>
    <circle cx="120" cy="386" r="4.5" fill="rgba(255,255,255,.2)" stroke="rgba(255,255,255,.45)" stroke-width="1"/>

    <!-- Right shoe -->
    <path d="M158 400 Q154 380 168 370 Q182 362 200 366 Q214 370 218 384 Q222 398 212 406 Q194 414 158 404Z" fill="url(#gShoeR)"/>
    <path d="M158 402 Q154 408 170 414 Q192 418 214 408 Q222 404 220 398 Q218 406 208 410 Q188 416 158 402Z" fill="#DCDCD0"/>
    <rect x="168" y="370" width="26" height="26" rx="3" fill="rgba(255,255,255,.11)"/>
    <line x1="169" y1="374" x2="193" y2="374" stroke="rgba(255,255,255,.55)" stroke-width="1.5" stroke-linecap="round"/>
    <line x1="169" y1="379" x2="193" y2="379" stroke="rgba(255,255,255,.48)" stroke-width="1.5" stroke-linecap="round"/>
    <line x1="169" y1="384" x2="193" y2="384" stroke="rgba(255,255,255,.42)" stroke-width="1.5" stroke-linecap="round"/>
    <ellipse cx="170" cy="400" rx="13" ry="5.5" fill="rgba(255,255,255,.28)"/>
    <circle cx="196" cy="382" r="4.5" fill="rgba(255,255,255,.18)" stroke="rgba(255,255,255,.38)" stroke-width="1"/>

    <!-- WHITE SOCKS -->
    <rect x="80" y="362" width="34" height="18" rx="10" fill="#F4F4F2"/>
    <rect x="163" y="356" width="34" height="18" rx="10" fill="#F4F4F2"/>
    <rect x="82" y="367" width="30" height="4" rx="2" fill="#E0E0E8"/>
    <rect x="165" y="361" width="30" height="4" rx="2" fill="#E0E0E8"/>

    <!-- ══ MUSTARD CHINOS ══ -->
    <path d="M90 222 L78 364 Q88 374 104 370 Q118 368 120 358 L120 222Z" fill="url(#gPants)"/>
    <path d="M162 222 L158 356 Q166 370 182 368 Q196 364 198 352 L200 222Z" fill="url(#gPants)"/>
    <path d="M90 222 L90 256 Q122 268 162 256 L162 222Z" fill="#B89030"/>
    <path d="M98 244 Q100 296 99 352" stroke="#907018" stroke-width="1.5" opacity=".55" stroke-linecap="round"/>
    <path d="M174 240 Q176 292 178 348" stroke="#907018" stroke-width="1.5" opacity=".55" stroke-linecap="round"/>
    <rect x="78" y="354" width="40" height="10" rx="4" fill="#A07820"/>
    <rect x="158" y="348" width="40" height="10" rx="4" fill="#A07820"/>

    <!-- ══ BACKPACK (behind right side) ══ -->
    <path d="M172 150 Q202 156 216 182 L220 270 Q220 292 204 296 L180 298 Q176 264 174 226Z" fill="url(#gBag)" filter="url(#fSoft)"/>
    <path d="M178 165 Q200 170 208 192 L212 248 Q200 236 188 230Z" fill="rgba(255,255,255,.07)"/>
    <rect x="178" y="218" width="36" height="50" rx="7" fill="#0C1428" stroke="rgba(255,255,255,.1)" stroke-width="1"/>
    <rect x="182" y="222" width="28" height="5" rx="2" fill="#C8A030" opacity=".6"/>
    <path d="M174 278 Q190 290 216 280 L220 268 Q202 278 174 268Z" fill="#7A4820"/>
    <path d="M178 280 Q192 284 212 278" stroke="#C8A030" stroke-width="1.5" fill="none" opacity=".5"/>

    <!-- Shoulder strap visible -->
    <path d="M174 150 Q178 186 178 218 Q178 254 182 280" stroke="#243060" stroke-width="16" stroke-linecap="round" fill="none"/>
    <path d="M174 150 Q178 186 178 218 Q178 254 182 280" stroke="rgba(255,255,255,.07)" stroke-width="6" stroke-linecap="round" fill="none"/>
    <rect x="172" y="192" width="12" height="7" rx="2.5" fill="#C8A030" stroke="#9A7820" stroke-width=".8"/>

    <!-- ══ T-SHIRT VISIBLE ══ -->
    <path d="M126 152 Q145 158 162 152 L164 224 Q148 230 134 224 Q124 220 122 224Z" fill="#EEECEA"/>

    <!-- ══ BOMBER JACKET ══ -->
    <!-- Left arm (raised, touching glasses) -->
    <path d="M82 158 Q58 172 48 200 Q40 222 52 238" stroke="url(#gJacketL)" stroke-width="32" stroke-linecap="round" fill="none"/>
    <path d="M52 238 Q44 256 52 270" stroke="#F4C5A0" stroke-width="24" stroke-linecap="round" fill="none"/>
    <!-- left hand -->
    <circle cx="56" cy="274" r="20" fill="url(#gFace)"/>
    <!-- finger touching glasses temple -->
    <path d="M44 265 Q38 255 44 248" stroke="#F4C5A0" stroke-width="9" stroke-linecap="round"/>
    <path d="M52 261 Q46 250 52 243" stroke="#F4C5A0" stroke-width="9" stroke-linecap="round"/>
    <path d="M61 260 Q57 249 63 243" stroke="#F4C5A0" stroke-width="8" stroke-linecap="round"/>
    <!-- Left white cuff -->
    <path d="M44 232 Q40 248 46 256 Q56 262 66 256 Q74 248 70 234Z" fill="#ECECEC"/>
    <path d="M46 238 Q50 248 62 246" stroke="rgba(0,0,0,.08)" stroke-width="1.5" fill="none"/>

    <!-- Right arm (holding backpack strap) -->
    <path d="M204 158 Q222 170 228 196 Q234 220 224 238" stroke="url(#gJacketR)" stroke-width="30" stroke-linecap="round" fill="none"/>
    <path d="M224 238 Q230 256 222 268" stroke="#F4C5A0" stroke-width="24" stroke-linecap="round" fill="none"/>
    <circle cx="218" cy="272" r="18" fill="url(#gFace)"/>
    <!-- Right white cuff -->
    <path d="M216 232 Q218 248 222 256 Q232 260 240 254 Q246 246 242 232Z" fill="#ECECEC"/>

    <!-- Jacket front body -->
    <path d="M90 152 Q116 162 150 160 Q184 162 210 152 L212 228 Q196 240 176 244 L124 244 Q104 240 88 228Z" fill="url(#gJacket)" filter="url(#fShadow)"/>
    <!-- jacket highlight left chest -->
    <path d="M100 162 Q116 166 130 162 L128 200 Q116 206 102 198Z" fill="rgba(255,255,255,.09)"/>
    <!-- jacket highlight right chest -->
    <path d="M168 162 Q184 166 198 162 L196 196 Q184 202 170 196Z" fill="rgba(255,255,255,.07)"/>
    <!-- center front zipper line -->
    <path d="M150 158 L150 240" stroke="#1A4A20" stroke-width="2" opacity=".7"/>
    <path d="M150 158 L134 168 L132 240" fill="rgba(0,0,0,.07)"/>
    <!-- zipper pull -->
    <rect x="147" y="190" width="7" height="10" rx="2.5" fill="#C8A030" opacity=".8"/>
    <rect x="148" y="188" width="5" height="4" rx="1.5" fill="#A07818"/>
    <!-- ribbed hem -->
    <rect x="88" y="232" width="126" height="14" rx="5" fill="#1A5020"/>
    <line x1="94" y1="234" x2="94" y2="244" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
    <line x1="100" y1="234" x2="100" y2="244" stroke="rgba(255,255,255,.11)" stroke-width="2"/>
    <line x1="106" y1="234" x2="106" y2="244" stroke="rgba(255,255,255,.11)" stroke-width="2"/>
    <line x1="112" y1="234" x2="112" y2="244" stroke="rgba(255,255,255,.1)" stroke-width="2"/>
    <line x1="190" y1="234" x2="190" y2="244" stroke="rgba(255,255,255,.11)" stroke-width="2"/>
    <line x1="196" y1="234" x2="196" y2="244" stroke="rgba(255,255,255,.1)" stroke-width="2"/>
    <line x1="202" y1="234" x2="202" y2="244" stroke="rgba(255,255,255,.1)" stroke-width="2"/>
    <!-- White collar stripe -->
    <path d="M112 152 Q132 160 150 159 Q168 160 188 152 L190 162 Q170 172 150 171 Q130 172 110 162Z" fill="#E8E8E8"/>
    <path d="M122 152 L150 159 L178 152 L176 158 L150 165 L124 158Z" fill="rgba(0,0,0,.05)"/>

    <!-- ══ NECK ══ -->
    <path d="M136 144 Q150 150 166 146 L164 158 Q150 164 138 160Z" fill="url(#gFace)"/>
    <path d="M140 144 Q150 149 162 146 L160 154 Q150 158 142 155Z" fill="rgba(150,70,20,.18)"/>

    <!-- ══ HEAD ══ -->
    <ellipse cx="150" cy="96" rx="58" ry="62" fill="url(#gFace)" filter="url(#fSoft)"/>

    <!-- Ears -->
    <ellipse cx="92" cy="100" rx="11" ry="15" fill="url(#gEar)"/>
    <ellipse cx="92" cy="100" rx="7" ry="10" fill="#E0A060"/>
    <path d="M88 93 Q86 100 88 107" stroke="#C08040" stroke-width="2" fill="none" stroke-linecap="round"/>
    <ellipse cx="208" cy="100" rx="11" ry="15" fill="url(#gEar)"/>
    <ellipse cx="208" cy="100" rx="7" ry="10" fill="#E0A060"/>
    <path d="M212 93 Q214 100 212 107" stroke="#C08040" stroke-width="2" fill="none" stroke-linecap="round"/>

    <!-- ══ HAIR (pompadour) ══ -->
    <!-- Dark base layer -->
    <path d="M94 82 Q96 40 150 34 Q204 40 206 82 L200 64 Q192 42 150 38 Q108 42 100 64Z" fill="#2A1008"/>
    <!-- Main pompadour volume -->
    <path d="M96 82 Q100 44 150 36 Q200 44 204 82 Q196 56 178 46 Q162 38 150 36 Q138 38 122 46 Q104 56 96 82Z" fill="url(#gHairT)"/>
    <!-- Pompadour front sweep (the signature volume) -->
    <path d="M108 64 Q118 30 150 24 Q178 22 196 44 Q208 60 206 78 Q190 52 170 44 Q154 36 146 38 Q128 40 112 64Z" fill="#924828"/>
    <!-- Hair highlight streak -->
    <path d="M128 38 Q142 28 158 34 Q152 42 138 48Z" fill="#C07840" opacity=".65"/>
    <!-- Hair texture strands -->
    <path d="M118 52 Q132 34 148 30" stroke="#C87840" stroke-width="2.5" fill="none" stroke-linecap="round" opacity=".55"/>
    <path d="M122 44 Q138 30 152 28" stroke="#C87840" stroke-width="1.8" fill="none" stroke-linecap="round" opacity=".45"/>
    <path d="M132 38 Q144 28 156 30" stroke="#D08848" stroke-width="1.5" fill="none" stroke-linecap="round" opacity=".4"/>
    <!-- Side hair taper -->
    <path d="M96 82 Q90 70 94 90 Q96 86 100 84Z" fill="#3A1808"/>
    <path d="M204 82 Q210 70 206 90 Q204 86 200 84Z" fill="#3A1808"/>
    <!-- Sideburns -->
    <path d="M94 90 Q90 100 92 112" stroke="#4A2010" stroke-width="6" stroke-linecap="round" fill="none"/>
    <path d="M206 90 Q210 100 208 112" stroke="#4A2010" stroke-width="6" stroke-linecap="round" fill="none"/>

    <!-- ══ EYEBROWS ══ -->
    <!-- Left (slightly furrowed inward = thinking) -->
    <path d="M110 75 Q122 68 134 72" stroke="#4A2010" stroke-width="4.5" stroke-linecap="round" fill="none"/>
    <!-- Right (slightly raised = curious) -->
    <path d="M164 72 Q176 66 188 70" stroke="#4A2010" stroke-width="4" stroke-linecap="round" fill="none"/>

    <!-- ══ EYES ══ -->
    <!-- Left eye -->
    <ellipse cx="122" cy="90" rx="13.5" ry="14.5" fill="white"/>
    <circle cx="123" cy="91" r="9.5" fill="url(#gEye)"/>
    <circle cx="123" cy="91" r="5.5" fill="#182038"/>
    <circle cx="127" cy="87" r="3" fill="rgba(255,255,255,.92)"/>
    <circle cx="120" cy="93" r="1.4" fill="rgba(255,255,255,.45)"/>
    <!-- eyelid shadow top left -->
    <path d="M108 86 Q122 81 136 86" stroke="#2A1008" stroke-width="2" fill="none" stroke-linecap="round" opacity=".6"/>
    <!-- lower lash line -->
    <path d="M109 95 Q122 100 135 95" stroke="#D09060" stroke-width="1.2" fill="none" stroke-linecap="round" opacity=".5"/>

    <!-- Right eye (slight upward gaze = thinking/looking up) -->
    <ellipse cx="178" cy="89" rx="13.5" ry="14.5" fill="white"/>
    <circle cx="180" cy="87" r="9.5" fill="url(#gEye)"/>
    <circle cx="180" cy="87" r="5.5" fill="#182038"/>
    <circle cx="184" cy="83" r="3" fill="rgba(255,255,255,.92)"/>
    <circle cx="177" cy="89" r="1.4" fill="rgba(255,255,255,.45)"/>
    <path d="M164 85 Q178 80 192 85" stroke="#2A1008" stroke-width="2" fill="none" stroke-linecap="round" opacity=".6"/>
    <path d="M165 93 Q178 98 191 93" stroke="#D09060" stroke-width="1.2" fill="none" stroke-linecap="round" opacity=".5"/>

    <!-- ══ ROUND GOLD GLASSES ══ -->
    <!-- Left lens -->
    <circle cx="122" cy="90" r="20" stroke="#C8A028" stroke-width="2.8" fill="rgba(180,220,255,.06)"/>
    <!-- Right lens -->
    <circle cx="178" cy="89" r="20" stroke="#C8A028" stroke-width="2.8" fill="rgba(180,220,255,.06)"/>
    <!-- Bridge -->
    <path d="M142 88 Q150 85 158 88" stroke="#C8A028" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <!-- Temple arms -->
    <path d="M102 89 Q96 91 92 96" stroke="#C8A028" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <path d="M198 88 Q204 90 208 96" stroke="#C8A028" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <!-- lens reflections -->
    <path d="M109 82 Q114 78 119 81" stroke="rgba(255,255,255,.55)" stroke-width="1.8" fill="none" stroke-linecap="round"/>
    <path d="M165 81 Q170 77 175 80" stroke="rgba(255,255,255,.5)" stroke-width="1.8" fill="none" stroke-linecap="round"/>

    <!-- ══ NOSE ══ -->
    <path d="M144 104 Q150 113 156 104" stroke="#C88050" stroke-width="2.8" fill="none" stroke-linecap="round"/>
    <ellipse cx="144" cy="106" rx="3.5" ry="2.5" fill="rgba(170,80,30,.22)"/>
    <ellipse cx="156" cy="106" rx="3.5" ry="2.5" fill="rgba(170,80,30,.22)"/>

    <!-- ══ FRECKLES ══ -->
    <circle cx="134" cy="100" r="1.8" fill="rgba(150,70,30,.28)"/>
    <circle cx="139" cy="105" r="1.4" fill="rgba(150,70,30,.22)"/>
    <circle cx="145" cy="97" r="1.4" fill="rgba(150,70,30,.22)"/>
    <circle cx="155" cy="100" r="1.8" fill="rgba(150,70,30,.28)"/>
    <circle cx="162" cy="105" r="1.4" fill="rgba(150,70,30,.22)"/>
    <circle cx="130" cy="104" r="1.2" fill="rgba(150,70,30,.18)"/>
    <circle cx="168" cy="103" r="1.2" fill="rgba(150,70,30,.18)"/>

    <!-- ══ CHEEKS ══ -->
    <ellipse cx="106" cy="108" rx="16" ry="10" fill="rgba(238,110,90,.17)"/>
    <ellipse cx="194" cy="106" rx="16" ry="10" fill="rgba(238,110,90,.17)"/>

    <!-- ══ SMILE (thoughtful half-smile) ══ -->
    <path d="M132 120 Q150 130 168 120" stroke="#B86848" stroke-width="3" stroke-linecap="round" fill="none"/>
    <path d="M136 122 Q150 130 162 122" fill="rgba(190,90,60,.13)"/>
    <path d="M142 125 Q150 130 158 125" stroke="rgba(255,255,255,.28)" stroke-width="1.8" fill="none" stroke-linecap="round"/>
  </svg>`;

  const wrapScene = (animClass, bubble, bStyle) => `
  <div class="char-scene fade-in">
    <div class="char-wrap" style="width:240px;height:344px">
      <div class="char-shadow" style="bottom:0;width:110px;left:50%;transform:translateX(-50%)"></div>
      <div class="${animClass}" style="position:relative">${svg}</div>
      <div class="char-bubble" style="${bStyle}">${bubble}</div>
    </div>
  </div>`;

  if (state === 'greet') {
    return `<div class="char-scene fade-in">
    <div class="char-wrap" style="width:240px;height:344px">
      <div class="char-shadow" style="bottom:0;width:110px;left:50%;transform:translateX(-50%)"></div>
      <svg class="sp1" style="position:absolute;top:14px;left:6px;width:22px;height:22px;overflow:visible" viewBox="0 0 20 20"><path d="M10 0l2.5 7.5H20l-6.5 4.5 2.5 7.5L10 15l-6 4.5 2.5-7.5L0 7.5h7.5z" fill="#FFD700"/></svg>
      <svg class="sp2" style="position:absolute;top:6px;right:10px;width:16px;height:16px;overflow:visible" viewBox="0 0 20 20"><path d="M10 0l2.5 7.5H20l-6.5 4.5 2.5 7.5L10 15l-6 4.5 2.5-7.5L0 7.5h7.5z" fill="#3056D3" opacity=".5"/></svg>
      <svg class="sp3" style="position:absolute;top:22px;right:28px;width:12px;height:12px;overflow:visible" viewBox="0 0 20 20"><path d="M10 0l2.5 7.5H20l-6.5 4.5 2.5 7.5L10 15l-6 4.5 2.5-7.5L0 7.5h7.5z" fill="#C83020" opacity=".4"/></svg>
      <div class="char-float" style="position:relative">${svg}</div>
      <div class="char-bubble" style="top:-4px;right:-18px">${greet[lang]}</div>
    </div>
  </div>`;
  }

  if (state === 'think') {
    return `<div class="char-scene fade-in">
    <div class="char-wrap" style="width:240px;height:344px">
      <div class="char-shadow" style="bottom:0;width:110px;left:50%;transform:translateX(-50%)"></div>
      <svg style="position:absolute;top:0;left:0;width:240px;height:344px;overflow:visible;pointer-events:none" viewBox="0 0 240 344">
        <text class="fq1" x="8" y="52" font-size="30" font-weight="900" fill="#3056D3" opacity=".5" font-family="Inter,sans-serif">?</text>
        <text class="fq2" x="196" y="40" font-size="24" font-weight="900" fill="#C83020" opacity=".45" font-family="Inter,sans-serif">?</text>
        <text class="fq3" x="184" y="76" font-size="17" font-weight="900" fill="#059669" opacity=".4" font-family="Inter,sans-serif">!</text>
      </svg>
      <div class="char-think" style="position:relative">${svg}</div>
      <div class="thought-dots" style="right:4px;top:22px">
        <div class="td td3"></div><div class="td td2"></div><div class="td td1"></div>
      </div>
      <div class="char-bubble" style="right:-14px;top:0px">${think[lang]}</div>
    </div>
  </div>`;
  }

  if (state === 'wait') {
    return `<div class="char-scene fade-in">
    <div class="char-wrap" style="width:240px;height:344px">
      <div class="char-shadow" style="bottom:0;width:110px;left:50%;transform:translateX(-50%)"></div>
      <div class="char-wait" style="position:relative">${svg}</div>
      <text class="fq1" style="position:absolute;left:12px;top:50px;font-size:14px;color:#3056D3;font-weight:800;opacity:.4">z</text>
      <text class="fq2" style="position:absolute;left:4px;top:36px;font-size:18px;color:#3056D3;font-weight:800;opacity:.3">z</text>
      <div class="char-bubble" style="right:-12px;top:4px">${wait[lang]}</div>
    </div>
  </div>`;
  }

  return '';
}

"""

with open('queue.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = '// ── CHARACTER ─────────────────────────────────────────────────────────────────'
end   = '// ── STATE ─────────────────────────────────────────────────────────────────────'

i1 = content.index(start)
i2 = content.index(end)

new_content = content[:i1] + NEW_CHAR + '\n\n' + content[i2:]

with open('queue.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done, new size:', len(new_content))
