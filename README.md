# birtday calendar

## what it does and how it works

- displays information about a person whose birthday is today, on a browser page
- the elements used for the page generation are defined in templates.py
- the browser page is generated at launch of main.py and on a new day
- the browser page is refreshes every minute

## input data

- input data must be in a .csv file formatted like example.csv at the root of the project
- videos can only be in .mp4 format, sound is muted on execution to use autoplay
- files referenced in the input file must be at the root of the project
- values lastname, firstname, birthdate and gender are required

## if you don't have python installed

- copy the executable for your system (supported are Windows and MacOS) into the root of this project
- run the executable instead of main.py

## start this app on login

### windows

- copy the main.exe from the dist folder to the project root
- create a task in the windows task scheduler
  - set the task to execute on startup
  - add main.exe as program to execute
  - set the working directory to the project root
