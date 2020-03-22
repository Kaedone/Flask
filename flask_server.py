#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, escape, url_for, render_template
from waitress import serve
from start import get_table

app = Flask(__name__)
@app.route('/get<param>')
def hello(param):
	return str(get_table(param))
if __name__ == "__main__":


    serve(app, port=8080)

    serve(app, host = "0.0.0.0", port = "8080")

    app.run(ssl_context='adhoc')
