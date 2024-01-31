# birtday calendar

## what it does and how it works

- displays information about a person whose birthday is today, on a browser page
- the elements used for the page generation are defined in templates.py
- the browser page is generated at launch of main.py and on a new day
- the browser page is refreshes every minute

## input data

- input data must be in a .csv file, formatted like example.csv, at the root of the project and named input.csv
- videos can only be in .mp4 format, sound is muted on execution to use autoplay
- image files can have the .png, .jpg or .jpeg extension
- files referenced in the input file must be at the root of the project
- values lastname, firstname, birthdate and gender are required

## if you don't have python installed

- get the executable for your system (supported are Windows and MacOS) from the latest [release](https://github.com/philipp-schuetz/birthday-calendar/releases/latest)
- copy the executable into the /src directory of this project
- run the executable instead of main.py

## start this app on login

### windows

- copy the windows executable from the latest release into the /src directory
- create a task in the windows task scheduler
  - set the task to execute on startup
  - add main.exe as program to execute
  - set the working directory to the project root

## program description (german only) up to date for v1.0.2
Der Geburtstagskalendar (birthday calendar) soll täglich aktuelle Geburtstage mit
Zusatzinformationen zu der betreffenden Person auf dem Bildschirm darstellen. Die
Darstellung erfolgt in einem Browserfenster, präferiert wird dabei der Browser
Mozilla Firefox. Dabei wird von dem Programm (kompilierte Version für MacOS und
Windows unter "/dist") einmal beim Start und danach täglich um ca. 00:00 Uhr eine
HTML-Datei nach definierten Vorlagen (templates.py) generiert, die dann
anschließend im Browser angezeigt wird. Für die Generierung der HTML-Datei wird
zu erst eine .csv Datei mit dem Namen "input.csv" (Beispiel: example.csv), die die
Geburtstage und weiteren Daten zu den jeweiligen Personen enthält, importiert. In
die Darstellung können auch Bilder oder Videos eingebunden werden. Videos sind
im Format .mp4 erlaubt und Bilder in den Formaten .png, .jpg und .jpeg. Diese
Dateien müssen sich im gleichen Ordner, wie das Programm befinden. Die, in der
input.csv angegebenen Daten müssen Vorname, Nachname, Geburtsdatum und
Geschlecht enthalten, alles Weitere ist optional. Anschließend werden die Daten auf
Richtigkeit bzw. die richtige Formatierung überprüft (Datum: 01.01.2000; Geschlecht:m, w, n; Dateien müssen existieren). Danach werden alle Daten für die weitere
Verwendung im Programm formatiert und unter Verwendung der Vorlagen in die
HTML-Datei geschrieben. Nach Vollendung der Generierung öffnet sich das
Browserfenster automatisch und aktualisiert sich minütlich, um die Veränderungen
der HTML-Datei darzustellen. Die Aktualisierung des Fensters könnte auch
ausschließlich um 00:00 Uhr erfolgen, dazu müsste jedoch JavaScript eingesetzt
werden, was eine weitere nicht unbedigt notwendige Komponente bedeuten würde.
Das Programm kann ohne Administratorrechte ausgeführt werden, deshalb muss
dieses durch den Nutzer in den Automatischen Start des Betriebssystems abgelegt
werden, wenn es nach einem Systemneustart automatich ausgeführt werden soll.
Eine nähere Beschreibung der verwendeten Strukturen lässt sich in Form von
Kommentaren im Quelltext des Projekts wiederfinden.