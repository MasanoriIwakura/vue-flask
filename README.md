# vue-flask

## Authoer

[MasanoriIwakura](https://github.com/MasanoriIwakura)

## Requirement

|Name|Viersion|
|:--|:--|
|Python|3.7|
|Pipenv|2018.7.1|
|Flask|1.0.2|
|Npm|6.3.0|
|Vue.js|2.5.2|

## Install

```bash
# Frontend Command
cd frontend
npm install
npm run build

# Backend Command
export PIPENV_VENV_IN_PROJECT=true
cd backend
pipenv install
pipenv run python do_create.py
cd ../
pipenv run python app.py
```

Access to http://localhost:5000

## Docker

```bash
# Docker build
docker build -t vue-flask .

# Docker run
docker run -d -p 80:5000 vue-flask
```

Access to http://localhost  
or  
Access to http://localhost/api/about