import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyDW3ushNaKA553JnM8n9XLB-7qKqK7i378",
  authDomain: "tgi-como.firebaseapp.com",
  projectId: "tgi-como",
  storageBucket: "tgi-como.firebasestorage.app",
  messagingSenderId: "719300062635",
  appId: "1:719300062635:web:b104903877f5d1037ff6ee",
  measurementId: "G-C1KQG9TXC6"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
