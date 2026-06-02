#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
═══════════════════════════════════════════════════════════════════
  CARICA OPERAI – T.G.I COMO (progetto Firebase: tgi-como)
═══════════════════════════════════════════════════════════════════

Crea gli account dei tecnici su Firebase Authentication e i relativi
documenti nella collezione 'utenti' di Firestore.

USA LE REST API di Firebase (nessun service-account / file json richiesto):
  - Identity Toolkit  → creazione utenti Auth
  - Firestore REST    → scrittura documento utente

CREDENZIALI ADMIN (per autenticare lo script):
  Email:    soluzioni@tgiitalia.com
  Password: TGI2026@

──────────────────────────────────────────────────────────────────
PREREQUISITI
  pip install requests
──────────────────────────────────────────────────────────────────
ISTRUZIONI
  1. Assicurati di aver già creato l'admin (apri setup.html una volta).
  2. Compila la lista OPERAI qui sotto.
  3. Esegui:  python3 carica_operai.py
──────────────────────────────────────────────────────────────────
"""

import requests
import sys

# ─── CONFIG FIREBASE (progetto tgi-como) ───────────────────────────
API_KEY     = "AIzaSyDW3ushNaKA553JnM8n9XLB-7qKqK7i378"
PROJECT_ID  = "tgi-como"

# ─── CREDENZIALI ADMIN ─────────────────────────────────────────────
ADMIN_EMAIL = "soluzioni@tgiitalia.com"
ADMIN_PASS  = "TGI2026@"

# ─── PASSWORD DI DEFAULT PER I NUOVI OPERAI ────────────────────────
# (ogni operaio potrà cambiarla dal login → "Cambia password")
PASSWORD_DEFAULT = "Tgi2026!"

# ═══════════════════════════════════════════════════════════════════
#  LISTA OPERAI DA CARICARE  →  compila qui
#  Ogni voce: nome, cognome, email
# ═══════════════════════════════════════════════════════════════════
OPERAI = [
    # {"nome": "Mario",  "cognome": "Rossi",  "email": "mario.rossi@tgiitalia.com"},
    # {"nome": "Luca",   "cognome": "Bianchi","email": "luca.bianchi@tgiitalia.com"},
]

# ═══════════════════════════════════════════════════════════════════
#  Da qui in giù NON serve modificare nulla
# ═══════════════════════════════════════════════════════════════════

IDTK = "https://identitytoolkit.googleapis.com/v1"
FS   = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents"


def login_admin():
    """Autentica l'admin e restituisce l'idToken."""
    r = requests.post(
        f"{IDTK}/accounts:signInWithPassword?key={API_KEY}",
        json={"email": ADMIN_EMAIL, "password": ADMIN_PASS, "returnSecureToken": True},
    )
    if r.status_code != 200:
        print("❌ Login admin fallito:", r.json().get("error", {}).get("message"))
        sys.exit(1)
    print("✅ Login admin OK")
    return r.json()["idToken"]


def crea_utente_auth(email, password):
    """Crea l'utente in Firebase Auth. Ritorna (uid, già_esistente)."""
    r = requests.post(
        f"{IDTK}/accounts:signUp?key={API_KEY}",
        json={"email": email, "password": password, "returnSecureToken": True},
    )
    if r.status_code == 200:
        return r.json()["localId"], False
    err = r.json().get("error", {}).get("message", "")
    if "EMAIL_EXISTS" in err:
        # Recupera l'uid facendo login con la password di default
        rl = requests.post(
            f"{IDTK}/accounts:signInWithPassword?key={API_KEY}",
            json={"email": email, "password": password, "returnSecureToken": True},
        )
        if rl.status_code == 200:
            return rl.json()["localId"], True
        return None, True   # esiste ma password diversa: non recuperabile qui
    print(f"   ❌ Errore Auth ({email}): {err}")
    return None, False


def scrivi_firestore(uid, nome, cognome, email, id_token):
    """Crea/aggiorna il documento utente in Firestore."""
    doc = {
        "fields": {
            "uid":          {"stringValue": uid},
            "nome":         {"stringValue": nome},
            "cognome":      {"stringValue": cognome},
            "nomeCompleto": {"stringValue": f"{nome} {cognome}"},
            "email":        {"stringValue": email},
            "ruolo":        {"stringValue": "operaio"},
        }
    }
    r = requests.patch(
        f"{FS}/utenti/{uid}",
        headers={"Authorization": f"Bearer {id_token}"},
        json=doc,
    )
    return r.status_code == 200


def main():
    if not OPERAI:
        print("⚠️  La lista OPERAI è vuota. Compila la lista nello script e riprova.")
        return

    id_token = login_admin()
    print(f"\n📋 Operai da processare: {len(OPERAI)}\n" + "─" * 50)

    creati, esistenti, errori = 0, 0, 0
    for op in OPERAI:
        nome    = op["nome"].strip()
        cognome = op["cognome"].strip()
        email   = op["email"].strip().lower()

        uid, gia = crea_utente_auth(email, PASSWORD_DEFAULT)
        if not uid:
            print(f"   ❌ {nome} {cognome} ({email}) — impossibile creare/recuperare")
            errori += 1
            continue

        ok = scrivi_firestore(uid, nome, cognome, email, id_token)
        if ok:
            if gia:
                print(f"   ↻ {nome} {cognome} ({email}) — già esistente, documento aggiornato")
                esistenti += 1
            else:
                print(f"   ✅ {nome} {cognome} ({email}) — creato")
                creati += 1
        else:
            print(f"   ⚠️  {nome} {cognome} ({email}) — Auth ok ma Firestore fallito")
            errori += 1

    print("─" * 50)
    print(f"\n🏁 Fine. Creati: {creati} | Già esistenti: {esistenti} | Errori: {errori}")
    print(f"\nPassword iniziale di ogni operaio: {PASSWORD_DEFAULT}")
    print("Ogni operaio potrà cambiarla dal login → 'Cambia password'.")


if __name__ == "__main__":
    main()
