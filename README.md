# Encounter-Generator

download and install git/python/vscode/docker/pgadmin

open docker then minimize

open repo in vscode or whatever you want

run in repo terminal:

python -m venv dev-env

then run: 

dev-env\Scripts\activate

you should see a green (dev-env) before PS  if running in windows

IF THIS DOESNT WORK CHECK YOUR POWERSHELL PERMISSIONS

run:
pip install django==3.1.0

(not necassary since docker installs django, but you get annoying errors in vscode for not having it installed in the vscode env or something idk)

docker-compose up -d --build

this builds a docker container and installs all packages in requirements.txt

open docker to see if web and db are running. If so check logs inside of the web container to verify the django app is running

127.0.0.0:8000 is the default port the site runs on in dev right now (docker lies)
