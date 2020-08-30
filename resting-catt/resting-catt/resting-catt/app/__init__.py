from flask import Flask, request, abort, jsonify, make_response
from catt.controllers import setup_cast
from catt.error import CastError

app = Flask(__name__)


@app.route("/")
def root():
    return {
        "msg": "Hello, there!"
    }


@app.errorhandler(422)
def unprocessable_entity(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(500)
def unprocessable_entity(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/cast_site", methods=['POST'])
def cast_site():
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
