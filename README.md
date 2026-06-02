# T.G.I COMO – Registro Ore Lavoro

App web (PWA) per la gestione delle ore di lavoro dei tecnici di **T.G.I COMO – Tank Gauging Italia**.

## Struttura

```
tgi-como/
├── index.html              # Login
├── registrati.html         # Registrazione nuovo tecnico
├── recupera-password.html  # Recupero password
├── operaio.html            # Area tecnico: inserimento ore + buste paga
├── admin.html              # Area admin: ore di tutti i tecnici + upload buste paga
├── setup.html              # Creazione account admin (eseguire UNA volta, poi eliminare)
├── manifest.json
├── sw.js
├── css/style.css
├── js/firebase-config.js   # Configurazione Firebase (progetto tgi-como)
├── js/pwa-install.js
└── img/, icon-*.png        # Logo e icone
```

## Pubblicazione su GitHub Pages

1. Crea un repository su GitHub (es. `ore` o `tgi-como`).
2. Carica tutti i file.
3. Settings → Pages → branch `main` / root.
4. URL tipo: `https://tuonome.github.io/ore/`.

> I percorsi in manifest.json e service worker sono RELATIVI (`./`),
> quindi l'app funziona con qualsiasi nome di repository.

## Primo avvio: crea l'admin

1. Apri `.../setup.html`
2. Clicca "Crea Admin T.G.I"
3. Al termine ELIMINA `setup.html` dal repository.

## Credenziali

- Admin   → Username: `TGI.ITALIA` | Email: `soluzioni@tgiitalia.com` | Password: `TGI2026@`
- Tecnici → si registrano da soli con la propria email da registrati.html

## Firebase (progetto tgi-como)

- Authentication → Email/Password (da abilitare nel pannello Firebase)
- Firestore → collezione `utenti` (+ sottocollezioni `mesi`, `bustePaga`)
- Storage → cartella `buste-paga/` per i PDF

## Funzioni

### Tecnico (operaio.html)
- Inserimento ore (inizio, fine, pausa, straordinario, cantiere)
- Calcolo automatico ore + statistiche mensili
- Download PDF del mese
- Archivio e visualizzazione delle proprie buste paga

### Admin (admin.html)
- Ore di tutti i tecnici, navigabili per mese
- Dettaglio per tecnico + PDF
- PDF cumulativo di tutti i tecnici
- Caricamento buste paga (PDF) per ogni tecnico

## Script Python (caricamento massivo operai)

Credenziali admin da usare nello script:
- Email:    soluzioni@tgiitalia.com
- Password: TGI2026@
