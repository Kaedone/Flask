#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# При изменении этих областей удалите файл token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Идентификатор и диапазон образца электронной таблицы.
SAMPLE_SPREADSHEET_ID = '1AwBuzkjz76_TCnVCKJMq8UL-ObRBC6m8BI3-NXeKiNI'

creds = None
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'credentials.json')
filename1 = os.path.join(dirname, 'token.pickle')

if os.path.exists(filename1):
    with open(filename1, 'rb') as token:
        creds = pickle.load(token)
    # Если нет (действительных) данных, то вход пользователя в систему.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            filename, SCOPES)
        creds = flow.run_local_server(port=0)
    # Сохранить учетные данные для следующего запуска
    with open(filename1, 'wb') as token:
        pickle.dump(creds, token)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


def get_teachers():
    range_teachers_id_name = 'Test!B4:C49'

    # Файл token.pickle хранит токены доступа пользователя и обновления и
    # создается автоматически при завершении потока авторизации для первого раза

    # Вызов листов с API

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_teachers_id_name).execute()
    values = result.get('values', [])

    sort = {
        'id': values[0],
        'teacherName': [1]
    }

    return sort


def get_schedule(teacher_id):
    teacher_id += 3
    teacher_id = str(teacher_id)
    range_teachers_id_name = 'Test!B{0}:CP{0}'.format(teacher_id)

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_teachers_id_name).execute()
    values = result.get('values', [])

    result = {
        'teacherID': values[0],
        'teacherName': values[1],
        'subject': values[3],
        'monday': values[4 - 20],
        'tuesday': values[20 - 40],
        'wednesday': values[40 - 58],
        'thursday': values[58 - 76],
        'friday': values[76 - 95]
    }

    return result


if __name__ == '__main__':
    data = int(0)

    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    get_teachers(data)
