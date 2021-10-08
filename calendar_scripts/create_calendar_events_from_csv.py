# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Modified by Andreia Ocanoaia
# Contact andreia.ocanoaia@gmail.com
# Original script https://github.com/googleworkspace/python-samples/blob/master/calendar/quickstart/quickstart.py

from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import argparse
import csv

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    # Populates Calendar entries from csv file, using Google Calendar API.
    parser = argparse.ArgumentParser(description='Populates Calendar entries from csv file, using Google Calendar API.')
    parser.add_argument('-i', '--input_file', type=str, required=True,
                        help="path to csv file with Calendar events")
    parser.add_argument('-c', '--calendar_id', type=str, required=True,
                        help="add the corresponding calendar id")
    parser.add_argument('-l', '--log_file', type=str, default='created-events.log',
                        help="path to log file")
    args = parser.parse_args()

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        # creds = None
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    events = get_events_from_csv_file(args.input_file)
    for event in events:
        event_result = service.events().insert(calendarId=args.calendar_id, body=event).execute()

def get_events_from_csv_file(csv_file):
    events = []
    return events

if __name__ == '__main__':
    main()
