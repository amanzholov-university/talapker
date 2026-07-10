const firebaseConfig = {
  apiKey: "AIzaSyDw7hWYvtUhNgMy5dUHbKCudKcAw8qbd44",
  authDomain: "talapker-43b91.firebaseapp.com",
  databaseURL: "https://talapker-43b91-default-rtdb.firebaseio.com",
  projectId: "talapker-43b91",
  storageBucket: "talapker-43b91.firebasestorage.app",
  messagingSenderId: "85928681389",
  appId: "1:85928681389:web:f8aa81d09e2502c3af0b24",
  measurementId: "G-XBVGNHMR9F"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
