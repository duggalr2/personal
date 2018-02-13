from __future__ import print_function
import httplib2
import os
import sqlite3
import dateutil.parser

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
# SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def fetch_events():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    min = datetime.datetime.utcnow().replace(hour=6, minute=00).isoformat() + 'Z' # 'Z' indicates UTC time
    max = datetime.datetime.utcnow().replace(hour=23, minute=50).isoformat() + 'Z'
    current_day = datetime.datetime.now().strftime("%A")

    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=min, timeMax=max, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')

    return current_day, events
    # for event in events:
    #     print(event['start'], event['summary'])

        # print(event['summary'])
        # time = event['start'].get('dateTime')
        # print(time)
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # print(start, event['summary'])


conn = sqlite3.connect('/Users/Rahul/Desktop/Side_projects/personal/db.sqlite3', check_same_thread=False)
c = conn.cursor()


def get_recent_p(tablename):
    c.execute('SELECT MAX(id) FROM %s' % tablename)
    line_recent_primary_key = c.fetchone()
    if line_recent_primary_key[0] is None:
        line_recent_primary_key = 1
    else:
        line_recent_primary_key = line_recent_primary_key[0]
    return line_recent_primary_key


def convert_google_time(google_time):
    dt = dateutil.parser.parse(google_time)
    return dt.strftime("%H:%M")


def add_day(current_day, day_pk):
    c.execute('INSERT INTO dashboard_day (id, day) VALUES (?, ?)', (day_pk+1, current_day))
    conn.commit()


def add_todoitem(todoitem_pk, current_day, start_time, end_time, todo_item):
    c.execute('INSERT INTO dashboard_todoitem (id, day_id, todo_item, start_time, end_time) VALUES (?, ?, ?, ?, ?)',
              (todoitem_pk, current_day, todo_item, start_time, end_time))
    conn.commit()


def main():
    day_pk = get_recent_p('dashboard_day')
    todoitem_pk = get_recent_p('dashboard_todoitem')
    current_day, events = fetch_events()
    add_day(current_day, day_pk)
    for event in events:
        start_time = event['start'].get('dateTime')
        end_time = event['end'].get('dateTime')
        start_time, end_time = convert_google_time(start_time), convert_google_time(end_time)
        todo_item = event['summary']
        todoitem_pk += 1
        add_todoitem(todoitem_pk, current_day, start_time, end_time, todo_item)


if __name__ == '__main__':
    main()



# add()

    # c.execute('INSERT INTO dashboard_day (id, day) VALUES (?, ?)', (day_pk+1, current_day))
    # conn.commit()


# c.execute('INSERT INTO dashboard_todoitem (id, day_id, todo_item, start_time, end_time) VALUES (?, ?, ?, ?, ?)',
#           (line_recent_primary_key, day, todo_item, start_time, end_time))
# conn.commit()

# class Day(models.Model):
#     day = models.CharField(max_length=500)
#
#
# class TodoItem(models.Model):
#     day = models.ForeignKey(Day, on_delete=models.CASCADE)
#     todo_item = models.CharField(max_length=2000)
#     start_time = models.TimeField()
#     end_time = models.TimeField()


# if __name__ == '__main__':
#     fetch_events()


# {'organizer': {'email': 'duggalr42@gmail.com', 'self': True},
#  'kind': 'calendar#event', 'creator': {'email': 'duggalr42@gmail.com', 'self': True},
# 'summary': 'ad', 'start': {'dateTime': '2018-02-13T11:00:00-05:00'},
# 'created': '2018-02-13T19:50:04.000Z', 'end': {'dateTime': '2018-02-13T14:30:00-05:00'},
# 'sequence': 0, 'id': '5roubr7l0iup4p0tgpob3g47pr', 'updated': '2018-02-13T19:50:04.950Z',
# 'status': 'confirmed', 'iCalUID': '5roubr7l0iup4p0tgpob3g47pr@google.com', 'etag': '"3037102809900000"',
# 'htmlLink': 'https://www.google.com/calendar/event?eid=NXJvdWJyN2wwaXVwNHAwdGdwb2IzZzQ3cHIgZHVnZ2FscjQyQG0',
# 'reminders': {'useDefault': True}}
