# -*- coding: UTF-8 -*-
from flask import Flask, send_from_directory, request
from flask.json import dumps
from faker import Faker

from faker_online.config import config

app = Flask(__name__, static_folder=config.STATIC_FOLDER)
app.config.from_object(config)
app.debug = config.DEBUG


def call(func):
    return func()


def serialize(obj):
    return str(obj)


@app.route('/api/<string:page>')
def api(page):
    fake = Faker(locale=request.args.get('locale', None))
    result = {'response': call(getattr(fake, page))}
    return dumps(result, default=serialize)


@app.route('/')
def index():
    return send_from_directory(config.STATIC_FOLDER + '/html', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
