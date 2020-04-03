#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SAMPLE_SPREADSHEET_ID = '1AwBuzkjz76_TCnVCKJMq8UL-ObRBC6m8BI3-NXeKiNI'

creds = None
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'credentials.json')
filename1 = os.path.join(dirname, 'token.pickle')
# Открываем token.pickle в котором лежит наши авторизационные данные
if os.path.exists(filename1):
    with open(filename1, 'rb') as token:
        creds = pickle.load(token)
# Если его нет, то открываем браузер и просим войти, что бы создать новый
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

    sort = json.dumps(values, sort_keys=True, indent=4)

    return sort


# Получаем рассписание для отдельного учителя
def get_schedule(teacher_id):
    if teacher_id < 0 or teacher_id > 46:
        return None
    teacher_id += 3
    teacher_id = str(teacher_id)
    range_teachers_id_name = 'Test!B{0}:CP{0}'.format(teacher_id)

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_teachers_id_name).execute()
    values = result.get('values', [])

    res = {
           "teacherID": values[0][1],
           "teacherName": values[0][2],
           "subject": values[0][3],
           "monday": values[0][4:20],
           "tuesday": values[0][20:40],
           "wednesday": values[0][40:58],
           "thursday": values[0][58:76],
           "friday": values[0][76:95]
           }
    y = json.dumps(res)

    return y


# Обрабатываем запрос из клиента
if __name__ == '__main__':
    data = int(0)

    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    get_teachers(data)
