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
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    SAMPLE_RANGE_NAME='Test!B'+idd.split(sep='=')[1]+':CP'+idd.split(sep='=')[1]
    creds = None
    print('Test!B'+idd.split(sep='=')[1]+':CP'+idd.split(sep='=')[1])
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    
    for x in range(len(values)):
    	pass

    return values

if __name__ == '__main__':
	data=int(0)
	main()
	with open("data_file.json", "r") as read_file:
		data = json.load(read_file)
	get_table(data)
