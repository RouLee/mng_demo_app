# Projekt-Anleitung: Flask + SQLite
Diese Demo-App zeigt, wie eine kleine Webapplikation mit **Flask** (Python) und einer **SQLite**-Datenbank funktioniert: Login/Registrierung sowie eine einfache Verwaltung von Tierbesitzer\*innen.

Die Anleitung besteht aus zwei Teilen:
- **Teil A – Lokal entwickeln:** Python und VSCode installieren und die App auf dem eigenen Computer starten.
- **Teil B – Online stellen (optional):** Die App im Team über GitHub und PythonAnywhere veröffentlichen.

## Projektstruktur

```
mng_demo_app/
├── flask_app.py       # Flask-App: alle Routen (Seiten)
├── auth.py            # Login, Registrierung, Benutzerverwaltung
├── db.py              # Verbindung zur SQLite-Datenbank + Hilfsfunktionen
├── db/TODOS.sql       # Datenbankschema + Beispieldaten
├── requirements.txt   # Benötigte Python-Pakete
├── templates/         # HTML-Vorlagen (Jinja2)
└── static/            # Bilder, Icons usw.
```

Die Datenbank ist eine einzelne Datei `db.sqlite3` im Projektordner. Sie wird beim ersten Start der App **automatisch erstellt** (inkl. Beispieldaten). Es muss kein Datenbankserver installiert werden.

------------------------------------------------------------------------

# Teil A – Lokal entwickeln (Nur auf Windows oder MacOS möglich, nicht auf Tablets)

## 1. Python installieren

Benötigt wird **Python 3.11 oder neuer**.

### Windows
1. https://www.python.org/downloads/ öffnen und die aktuelle Version herunterladen.
2. Installer starten.
3. **Wichtig:** Ganz unten das Häkchen bei **„Add python.exe to PATH“** setzen.
4. Auf **„Install Now“** klicken.
5. Kontrolle: Eine neue Eingabeaufforderung (PowerShell) öffnen und eingeben:
   ```
   python --version
   ```
   Es sollte z.B. `Python 3.13.x` erscheinen.

>  Öffnet sich stattdessen der Microsoft Store, wurde Python nicht zum PATH hinzugefügt. Installer erneut starten → *Modify* → *Add Python to environment variables* aktivieren, oder unter *Einstellungen → Apps → Erweiterte App-Einstellungen → App-Ausführungsaliase* die Einträge für `python.exe` deaktivieren.

### macOS
1. https://www.python.org/downloads/ öffnen und den macOS-Installer herunterladen.
2. Installer ausführen.
3. Kontrolle im Terminal:
   ```
   python3 --version
   ```
   Auf macOS heisst der Befehl `python3` (statt `python`) – in den folgenden Schritten entsprechend anpassen.

### Alternative: Anaconda / Miniconda
Wer bereits **Anaconda** oder **Miniconda** installiert hat, kann auch eine conda-Umgebung verwenden (siehe Schritt 4, Variante B).

------------------------------------------------------------------------

## 2. VSCode und Erweiterungen installieren

### 2.1 VSCode installieren
1.  https://code.visualstudio.com/ öffnen, herunterladen und installieren.
2. Windows: Im Installer die Optionen **„Zu PATH hinzufügen“** und **„Mit Code öffnen“** aktivieren.

### 2.2 Erweiterungen installieren
1. VSCode öffnen.
2. Links in der Seitenleiste auf das Symbol **Erweiterungen** klicken (vier Quadrate) oder `Ctrl+Shift+X` (macOS: `Cmd+Shift+X`).
3. Folgende Erweiterungen suchen und auf **Install** klicken:

| Erweiterung | Herausgeber | Wofür? |
|---|---|---|
| **Python** | Microsoft | Python-Unterstützung, Ausführen, Debuggen (installiert *Pylance* und *Python Debugger* automatisch mit) |
| **SQLite Viewer** | Florian Klampfer | Optional: Die Datei `db.sqlite3` direkt in VSCode anschauen |

------------------------------------------------------------------------

## 3. Git installieren

Mit **Git** wird der Code von GitHub heruntergeladen (geklont) und später Änderungen synchronisiert.

### Windows
1. https://git-scm.com/downloads/win öffnen und den **64-bit Git for Windows Setup** herunterladen.
2. Installer starten und überall die Standardeinstellungen mit **Next** bestätigen, am Schluss auf **Install** klicken.
3. Kontrolle: VSCode bzw. eine neue PowerShell öffnen und eingeben:
   ```
   git --version
   ```
   Es sollte z.B. `git version 2.x.x.windows.x` erscheinen.

### macOS
1. Im Terminal eingeben:
   ```
   git --version
   ```
2. Ist Git noch nicht installiert, erscheint ein Fenster zur Installation der **Command Line Developer Tools** → auf **Installieren** klicken und warten.
   Alternativ mit Homebrew: `brew install git`

### Git einrichten (einmalig)
Name und E-Mail-Adresse setzen (dieselbe E-Mail wie beim GitHub-Account verwenden):
```
git config --global user.name "Vorname Nachname"
git config --global user.email "deine.email@beispiel.ch"
```

------------------------------------------------------------------------

## 4. Git Repository clonen

Beim **Clonen** wird eine lokale Kopie eines bestehenden GitHub-Repositories erstellt.

### 4.1 Repository-URL kopieren
1. Das Repository auf GitHub öffnen (z.B. https://github.com/yourUserName/db-projekt-3x bzw. euer eigenes Repository/Fork).
2. Auf den grünen Button **Code** klicken.
3. Reiter **HTTPS** wählen und die URL kopieren, z.B. `https://github.com/dein_github_username/dein_repo.git`

### 4.2 Clonen in VSCode
1. VSCode öffnen und `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`) drücken.
2. **„Git: Clone“** eingeben und auswählen.
3. Die kopierte URL einfügen und mit `Enter` bestätigen.
4. Einen Ordner wählen, in dem das Repository gespeichert werden soll (z.B. `C:\Users\<Name>\Repositories`), und auf **Select as Repository Destination** klicken.
5. Beim ersten Mal öffnet sich ein Fenster, um sich bei **GitHub anzumelden** → **Sign in with browser** bzw. **Allow** und im Browser bestätigen.
6. Auf die Frage *„Would you like to open the cloned repository?“* auf **Open** klicken.

## 5. Projekt herunterladen und in VSCode öffnen


1. Von https://github.com/RouLee/mng_demo_app rechts oben auf **Code** → **Download ZIP** klicken.
2. ZIP-Datei in eurem Ordner des lokalen Repositories entpacken.
3. VSCode öffnen → **Datei → Ordner öffnen** → den entpackten Ordner auswählen.
4. Falls oben die Meldung kommt ob man der Umgebung vertrauen möchte, auf **Trust** klicken.


------------------------------------------------------------------------

## 6. Python-Umgebung einrichten und Pakete installieren

Damit die Pakete des Projekts nicht mit anderen Projekten vermischt werden, wird eine eigene Umgebung verwendet.

### Variante A: venv (Python von python.org)
Im VSCode-Terminal ("View → Terminal")

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Meldet PowerShell *„Die Ausführung von Skripts ist auf diesem System deaktiviert“*, einmalig folgenden Befehl ausführen und danach erneut aktivieren:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```

Ist die Umgebung aktiv, steht im Terminal `(.venv)` vor der Eingabezeile.

### Interpreter in VSCode auswählen
1. `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`) drücken.
2. **„Python: Select Interpreter“** eingeben und auswählen.
3. Die eben erstellte Umgebung wählen (`.venv` bzw. die conda-Umgebung).

Unten rechts in der Statusleiste wird nun die gewählte Python-Version angezeigt.

------------------------------------------------------------------------

##  7. App starten

Im VSCode-Terminal (mit aktiver Umgebung):
```
python flask_app.py
```

Alternativ: `flask_app.py` öffnen und oben rechts auf den  **Run**-Button klicken.

Im Terminal erscheint u.a.:
```
 * Running on http://127.0.0.1:5000
```

1. Im Browser **http://127.0.0.1:5000** öffnen.
2. Auf **Registrieren** klicken und einen Benutzer anlegen.
3. Einloggen – nun erscheint die Liste der Besitzer\*innen.

Die App läuft im **Debug-Modus**: Änderungen am Code werden automatisch neu geladen. Beenden mit `Ctrl+C` im Terminal.

------------------------------------------------------------------------

## 8. Datenbank

- Die Datenbank liegt in der Datei **`db.sqlite3`** im Projektordner und wird beim ersten Start automatisch aus `db/TODOS.sql` erstellt.
- **Anschauen:** Mit der Erweiterung *SQLite Viewer* einfach `db.sqlite3` in VSCode anklicken.
- **Schema ändern:** `db/TODOS.sql` anpassen und die Datenbank neu erstellen.
- **Zurücksetzen / neu erstellen:**
  ```
  python db.py
  ```
  Dabei werden **alle Daten gelöscht** (auch registrierte Benutzer) und die Beispieldaten neu eingefügt.
- `db.sqlite3` ist in `.gitignore` eingetragen und wird **nicht** auf GitHub hochgeladen – jede Person hat ihre eigene lokale Datenbank.


------------------------------------------------------------------------

# Teil B – Im Team online stellen (PythonAnywhere, optional oder für Tablet-Benutzer)

**Hinweis:** Nur eine Person pro Team muss diesen Teil durchführen.

## Voraussetzungen

-   Alle Teammitglieder besitzen einen **GitHub-Account**
-   **Eine Person** besitzt einen **PythonAnywhere-Account**
-   Diese Person teilt das PythonAnywhere-Login **mit dem Team** (damit alle deployen können)

## 1. PythonAnywhere vorbereiten
https://www.pythonanywhere.com

### 2.2 Neue Flask-Webapp erstellen
1.	Menü: Web → Add new web app
2.	Flask auswählen
3.	Python 3.13 auswählen

### 2.3 Webapp-Verzeichnis ersetzen
1.	Zurück auf das Dashboard
2.	Jetzt Terminal öffnen\ → Open Bash Console (links auf den Button $ Bash) klicken.

``` bash
# Das von GitHub geforkte Repo klonen
git clone https://github.com/dein_github_username/dein_repo.git

# Alte Struktur löschen
rm -rf mysite

# Neuen Code als Webapp-Verzeichnis verwenden
mv <dein_repo> mysite

# Benötigte Pakete installieren
pip3.13 install --user -r mysite/requirements.txt


## 3. Datenbank
Es ist **keine Einrichtung nötig**: Die SQLite-Datei `mysite/db.sqlite3` wird beim ersten Aufruf der Webseite automatisch erstellt.

Zum Zurücksetzen in einer Bash-Console:
```bash
cd mysite
python3.13 db.py
```
Danach im Menü *Web* auf **Reload** klicken.


## 4. Website testen
1. Rufe die URL http://<username_pythonanywhere>.pythonanywhere.com auf.
2. Siehst du ein Login? Klicke auf registrieren und registriere einen User
3. Falls du noch die Message "Welcome to Flask!" siehst, gehe zurück zum Menü "Web" und klicke auf  Reload

## 5. Website aktualisieren

Auf PythonAnywhere:
```bash
cd mysite
git pull
pip3.13 install --user -r requirements.txt
```
Danach im Menü von PythonAnywhere *Web* auf  **Reload** klicken.