#!/usr/bin/python
# -*- coding: utf-8 -*-

# Импортируем всё, что нам нужно для запуска сервера
from flask import Flask

#  Подключпем сам файл с запросами и другим кодом
from start import get_teachers, get_schedule

app = Flask(__name__)


# Получение рассписания конкретного учителя
@app.route('/schedule/<schedule_id>')
def hello(schedule_id):
    return get_schedule(int(schedule_id))


# Получение всех учителей и их id
@app.route('/all_teachers')
def teacher_handler():
    return get_teachers()


# Настройка портов и хоста
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
