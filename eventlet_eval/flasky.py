from flask import Flask, jsonify

from eventlet_eval import aws


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def get_ecs_regions():
        result = aws.list_ecs_clusters("us-east-1")
        return jsonify(result)

    return app
