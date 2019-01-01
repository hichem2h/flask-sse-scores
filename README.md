# Scores

Scores application is an example of sse (Server Side Events) backend using Flask and gevent in addition to its implementation in Javascript

## How to use

    virtualenv venv

    # activate your virtual environment

    pip install -r requirements.txt

    cd flask-sse-backend

    python gevent_server.py


## Routes

* / ==> Home Page
* /add ==> Add new score
* /update/score_id ==> Update score