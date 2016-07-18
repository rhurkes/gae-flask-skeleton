import flask
from flask import Response, redirect, render_template, request, make_response
from flask.ext.cors import CORS

application = flask.Flask(__name__)
application.url_map.strict_slashes = False

cors = CORS(application)


@application.route("/", methods=['GET'])
def home():
    return "Hello World!"

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True, threaded=True, port=8080)
