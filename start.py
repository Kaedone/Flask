#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json


# При изменении этих областей удалите файл token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Идентификатор и диапазон образца электронной таблицы.
SAMPLE_SPREADSHEET_ID = '1AwBuzkjz76_TCnVCKJMq8UL-ObRBC6m8BI3-NXeKiNI'


def get_table(idd):
    
    SAMPLE_RANGE_NAME='Test!B'+idd.split(sep='=')[1]+':CP'+idd.split(sep='=')[1]
    creds = None
    print('Test!B'+idd.split(sep='=')[1]+':CP'+idd.split(sep='=')[1])
    # Файл token.pickle хранит токены доступа пользователя и обновления и
    # создается автоматически при завершении потока авторизации для первого
    # раза
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Если нет (действительных) данных, пусть вход пользователя в систему.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Сохранить учетные данные для следующего запуска
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    # Вызов листов с API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    
    for x in range(len(values)):
    	pass

    return values

if __name__ == '__main__':
	data=int(0)
	
	with open("data_file.json", "r") as read_file:
		data = json.load(read_file)
	get_table(data)
