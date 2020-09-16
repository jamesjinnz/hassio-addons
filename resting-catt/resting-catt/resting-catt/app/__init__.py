import logging

from flask import Flask, request, abort, jsonify
from catt.controllers import setup_cast
from catt.error import CastError
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route("/")
def root():
    return {
        "msg": "Hello, there!"
    }


@app.errorhandler(422)
@app.errorhandler(500)
def handle_http_error(error):
    response = jsonify({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    response.status_code = error.code
    return response


@app.route("/cast_site", methods=['POST'])
def cast_site():
    app.logger.info(f"Request: {str(request)}")
    data = request.json
    if all(key in data for key in ('device', 'url')):
        try:
            cst = setup_cast(data['device'],
                             controller="dashcast",
                             action="load_url",
                             prep="app")
            cst.load_url(data['url'])
            return '', 204
        except CastError as e:
            abort(500, e)

    else:
        abort(422, 'device and url is required in post data')

def run():
    app.run(port=9898, host='0.0.0.0')
