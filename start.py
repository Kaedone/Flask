#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# Ссылка на аутенфикацию
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# ID вашей таблицы (стоит в адресной строке)
SAMPLE_SPREADSHEET_ID = '1AwBuzkjz76_TCnVCKJMq8UL-ObRBC6m8BI3-NXeKiNI'

creds = None
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'credentials.json')
filename1 = os.path.join(dirname, 'token.pickle')
# Открываем token.pickle в котором лежит наши авторизационные данные
if os.path.exists(filename1):
    with open(filename1, 'rb') as token:
        creds = pickle.load(token)
# Если его нет, то открываем браузер и просим войти, что бы создать новый token.pickle
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            filename, SCOPES)
        creds = flow.run_local_server(port=0)
    # Сохраняем учетные данные для следующего запуска
    with open(filename1, 'wb') as token:
        pickle.dump(creds, token)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


# Получаем список всех учителей
def get_teachers():
    # Обратите внимание! Test-название листа в таблице !-разделитель B4:C49-диапазон
    range_teachers_id_name = 'Test!B4:D49'

    # Создаём массив с результатами
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_teachers_id_name).execute()
    values = result.get('values', [])

    # Делаем крассивый вывод
    sort = json.dumps(values, sort_keys=True, indent=4)

    return sort


# Получаем рассписание для отдельного учителя
def get_schedule(teacher_id):
    # Если нам прислали не действительный id то выкидываем ошибку
    if teacher_id < 0 or teacher_id > 46:
        return None
    # Делаем из это строчку
    teacher_id += 3
    teacher_id = str(teacher_id)
    range_teachers_id_name = 'Test!B{0}:CQ{0}'.format(teacher_id)

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_teachers_id_name).execute()
    values = result.get('values', [])
    # Генерируем из этого словарь для удобности вывода
    res = {
        "teacherID": values[0][0],
        "teacherName": values[0][1],
        "subject": values[0][2],
        "monday": values[0][3:19],
        "tuesday": values[0][19:39],
        "wednesday": values[0][39:57],
        "thursday": values[0][57:75],
        "friday": values[0][75:93],
        "photo": values[0][93]
    }
    # Генерим это в крассивый .json
    y = json.dumps(res)

    return y


# Возвращаем длительность урока
def timing():
    time_of_lessons = 'Test!U2:AN2'

    # Создаём массив с результатами
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=time_of_lessons).execute()
    values = result.get('values', [])

    # Генерим крассивый .json
    sort = json.dumps(values, sort_keys=True, indent=4)

    return sort


# Обрабатываем запрос из клиента
if __name__ == '__main__':
    data = int(0)

    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    get_teachers(data)
