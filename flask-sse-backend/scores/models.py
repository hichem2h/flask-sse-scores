

class Score:

    def __init__(self, id, team1, team2, score):
        self.id = id
        self.team1 = team1
        self.team2 = team2
        self.score = score

    def __str__(self):
        return f'{self.team1} = {self.score} = {self.team2}'


class ScoreEvent:

    def __init__(self, score):
        self.score = score

    def encode(self):
        lines = []

        lines.append(f'data: {self.score}')
        lines.append(f'id:{self.score.id}')

        return "\n".join(lines) + "\n\n"
