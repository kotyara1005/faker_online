# -*- coding: UTF-8 -*-
from flask import Flask, send_from_directory

from faker_online.config import config

app = Flask(__name__, static_folder=config.STATIC_FOLDER)
app.config.from_object(config)
app.debug = config.DEBUG


@app.route('/')
def index():
    return send_from_directory(config.STATIC_FOLDER + '/html', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
