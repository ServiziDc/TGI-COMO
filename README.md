# T.G.I COMO – Registro Ore Lavoro

App web (PWA) per la gestione delle ore di lavoro dei tecnici di **T.G.I COMO – Tank Gauging Italia**.

## Struttura

```
tgi-como/
├── index.html              # Login
├── registrati.html         # Registrazione nuovo tecnico
├── recupera-password.html  # Recupero password
├── operaio.html            # Area tecnico: inserimento ore
├── admin.html              # Area admin: ore di tutti i tecnici
├── setup.html              # Creazione account admin (eseguire UNA volta, poi eliminare)
├── manifest.json
├── sw.js
├── firestore.rules         # Regole di sicurezza Firestore (da incollare in Firebase)
├── css/style.css
├── js/firebase-config.js   # Configurazione Firebase (progetto tgi-como)
├── js/pwa-install.js
└── img/, icon-*.png        # Logo e icone
```

## Pubblicazione su GitHub Pages

1. Carica tutti i file nel repository.
2. Settings → Pages → branch `main` / root.
3. URL tipo: `https://servizidc.github.io/TGI-COMO/`.

## Firebase (progetto tgi-como) — TUTTO GRATIS

Serve solo il piano gratuito (Spark). NON serve Storage né pagamenti.

1. **Authentication** → abilita **Email/Password**.
   In Authentication → Settings → Authorized domains aggiungi `servizidc.github.io`.
2. **Firestore Database** → Create database (regione `europe-west`).
   Nella scheda **Rules** incolla il contenuto di `firestore.rules` e pubblica.

## Primo avvio: crea l'admin

1. Apri `.../setup.html`
2. Clicca "Crea Admin T.G.I"
3. Al termine ELIMINA `setup.html` dal repository.

## Credenziali

- Admin   → Username: `TGI.ITALIA` | Email: `soluzioni@tgiitalia.com` | Password: `TGI2026@`
- Tecnici → si registrano da soli con la propria email da registrati.html

## Funzioni

### Tecnico (operaio.html)
- Inserimento ore (inizio, fine, pausa, straordinario, cantiere)
- Calcolo automatico ore + statistiche mensili
- Download PDF del mese

### Admin (admin.html)
- Ore di tutti i tecnici, navigabili per mese
- Dettaglio per tecnico + PDF
- PDF cumulativo di tutti i tecnici

## Script Python (caricamento massivo operai)

Credenziali admin da usare nello script `carica_operai.py`:
- Email:    soluzioni@tgiitalia.com
- Password: TGI2026@
