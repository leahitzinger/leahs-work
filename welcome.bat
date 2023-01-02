echo off
:: this file takes in 2 arguments name 
set name=%1
set teacher=%2
::showing that bat startet running
echo script started
::reading in a python file
python welcome.py %name% %teacher%
::openning slack
start C:/Users/admin/AppData/Local/slack/slack.exe
:: creating and openning docx file
echo Welcome to class! This is for taking notes >notes.docx
start notes.docx
::showing that bat finished running
echo script completed



