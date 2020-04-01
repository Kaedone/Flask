#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, escape, url_for, render_template, request
from waitress import serve
from start import get_table

app = Flask(__name__)


@app.route('/get')
def hello():
    teachers = request.args.get('page', default=0, type=int)
    return get_table(teachers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
