Alles klar. Hier ist eine kompakte, vollständige Entwickler-Übergabe (Technical Brief) für dein Projekt „Black Pearl GmbH – Vermittlungsplattform“. Dieser Text ist ideal, um ihn einem externen Programmierer oder Entwicklungsteam zu schicken – egal ob Freelancer oder Agentur.


---

🖥️ Projektname: Black Pearl GmbH – Digitale Vermittlungsplattform


---

🎯 Ziel des Projekts:

Eine skalierbare Web-App zur Vermittlung von Personal in den Bereichen Gastronomie, Pflege und Bau, mit vier klar definierten Nutzergruppen und automatisierten Abläufen – inklusive Matching, Kommunikation, Abrechnung, Kalender und Bewertungen.


---

👥 Nutzergruppen & Rollen:

1. Veranstalter (Auftraggeber):

Erstellen von Einsätzen (Datum, Ort, Jobbeschreibung, Anforderungen)

Matching & Buchung von Freelancern oder Agenturen

Kommunikation via Chat

Kalenderübersicht & Rechnungsdownload

Bewertung nach Abschluss



2. Freelancer / Mietpersonal:

Verfügbarkeit eintragen

Jobs sehen & annehmen

Arbeitszeiten dokumentieren

Chat mit Veranstalter

Verdienstübersicht & Bewertungsübersicht



3. Personaldienstleister (Agenturen):

Verwaltung von Freelancer-Pools

Zuordnung von Kräften auf Aufträge

Provision festlegen

Statistiken & Exporte

Kommunikation mit allen Beteiligten



4. Admin (Plattformbesitzer):

Nutzer-Management & Buchungsüberwachung

Auszahlungskontrolle (Stripe)

Blacklist / Sicherheit / Eskalation

Provisionen / Rechnungen / Exporte

Live-Monitoring & Plattform-Statistik





---

🔑 Hauptfunktionen der Plattform:

✅ Registrierung / Login für alle Rollen

✅ Rollenbasierte Dashboards (React)

✅ Job-Matching basierend auf Ort, Verfügbarkeit, Skills

✅ Echtzeit-Chat (Socket.IO)

✅ Kalenderansicht mit Filter

✅ Bewertungen mit Sternen & Kommentaren

✅ Stripe-Integration (7 Tage Auszahlung)

✅ Automatische Rechnungserstellung

✅ Upload von Zertifikaten / Verträgen

✅ Adminpanel mit Exporte, Nutzerübersicht, Provisionskontrolle

✅ QR-Code-Integration für z. B. Visitenkarte mit eingebetteter schwarzer Perle (nur eine, realistisch)



---

🧱 Tech Stack (Vorgabe):

Frontend: React.js, Tailwind CSS, Zustand/Redux (optional), mobile responsive, Glassmorphism-Design

Backend: Node.js + Express.js

Datenbank: MongoDB (Mongoose)

Auth: JWT (rollenbasiert)

Live-Kommunikation: Socket.IO

Zahlung: Stripe (Test- & Live-Modus)

Hosting (Demo): Vercel / Render

Späterer Hosting-Vorschlag: Hetzner Cloud oder AWS (DSGVO-konform)



---

🎨 Designrichtlinien (verbindlich):

Farben: Schwarz (Haupt), Gold (Akzent)

Designstil: Glassmorphism (transparente UI, Blur-Effekte)

Logo/Visitenkarte: Nur eine schwarze Perle, eingebettet im QR-Code. Niemals doppelt.

Schrift: Elegant, gut lesbar – keine verspielten Fonts

Responsiveness: Mobil-first, aber auch Desktop-optimiert



---

🔐 Sicherheit / DSGVO:

SSL-Verschlüsselung

Kein Tracking / kein 3rd-Party-Analytics

Rollenbasierte Zugriffskontrolle

Upload-Verifizierung (PDF, ID, Verträge)

Spätere Anbindung an externe Audit-Systeme möglich



---

📎 Anhang:

Der gesamte Start-Code (Auth, Backend-Logik, Datenmodelle, Chat, Stripe, Login-UI) ist bereits vorbereitet.
👉 Hier klicken für den kompletten Code


---

🔄 Weitere Erweiterungen möglich:

Mobile App (React Native oder Flutter)

iCal-Export für Veranstalter

Push-Nachrichten (Firebase / OneSignal)

Automatisiertes Bewertungssystem

Multilingualität (Deutsch, Englisch, Polnisch)
