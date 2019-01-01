from flask import Flask
from .conf import config


def create_app():
    app = Flask(__name__)

    app.config.from_object(config[app.env])

    from scores import bp as scores_bp
    app.register_blueprint(scores_bp)

    @app.route('/health')
    def health():
        return 'OK'

    return app
