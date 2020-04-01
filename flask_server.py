#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask

from start import get_teachers, get_schedule

app = Flask(__name__)


@app.route('/schedule/<schedule_id>')
def hello(schedule_id):
    return get_schedule(int(schedule_id))


@app.route('/all_teachers')
def teacher_handler():
    return get_teachers()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
