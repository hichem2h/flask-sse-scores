from flask import Response, render_template, request, redirect

from scores import bp
from scores.models import ScoreEvent, Score

from gevent.queue import Queue

scores = [Score(0, 'FC Barcelona', 'Chelsea', '2-1'),
          Score(1, 'Real Madrid', 'Manchester City', '0-0')]

subscriptions = []


@bp.route('/stream')
def stream():
    def generate():
        queue = Queue()
        subscriptions.append(queue)
        try:
            while True:
                result = queue.get()
                ev = ScoreEvent(result)
                yield ev.encode()
        except GeneratorExit:
            subscriptions.remove(queue)

    return Response(generate(), mimetype='text/event-stream')


@bp.route('/')
def home():
    return render_template('scores/index.html', scores=scores)


@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        team1 = request.form.get('team1', None)
        team2 = request.form.get('team2', None)
        score = request.form.get('score', None)

        if team1 and team2 and score:
            id = len(scores)
            score = Score(id, team1, team2, score)
            scores.append(score)

            notify(score)

            redirect('/')

    return render_template('scores/add.html')


@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        team1 = request.form.get('team1', None)
        team2 = request.form.get('team2', None)
        score = request.form.get('score', None)

        if team1 and team2 and score:
            score = Score(id, team1, team2, score)
            scores[id] = score

            notify(score)

            redirect('/')

    if id >= len(scores):
        return 'Not found', 404

    return render_template('scores/update.html', score=scores[id])


def notify(score):
    for sub in subscriptions:
        sub.put(score)


# def check_connections():
#     while True:
#         gevent.sleep(5)
#         for sub in subscriptions:
#             sub.put(None)


# gevent.Greenlet.spawn(check_connections)
