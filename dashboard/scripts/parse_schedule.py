import sqlite3

conn = sqlite3.connect('/Users/Rahul/Desktop/Side_projects/personal/db.sqlite3', check_same_thread=False)
c = conn.cursor()

f = open('schedule')
lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]

days = ['Monday:', 'Tuesday:', 'Wednesday:', 'Thursday:', 'Friday:', 'Saturday:', 'Sunday:']

temp = []
index_temp = 0

c.execute('SELECT MAX(id) FROM dashboard_day')
day_recent_primary_key = c.fetchone()
if day_recent_primary_key[0] is None:
    day_recent_primary_key = 1
else:
    day_recent_primary_key = day_recent_primary_key[0]

c.execute('SELECT MAX(id) FROM dashboard_todoitem')
line_recent_primary_key = c.fetchone()
if line_recent_primary_key[0] is None:
    line_recent_primary_key = 1
else:
    line_recent_primary_key = line_recent_primary_key[0]

for line in lines:
    if line in days:
        day_recent_primary_key += 1
        temp.append(line[:-1])
        c.execute('INSERT INTO dashboard_day (id, day) VALUES (?, ?)', (day_recent_primary_key, line[:-1]))
        conn.commit()
        index_temp = temp.index(line[:-1])
    if '- ' in line:
        line_recent_primary_key += 1
        day = temp[index_temp]
        line = line.split(' ')
        start_time = line[1]
        end_time = line[3][:-1]
        todo_item = ' '.join(line[4:])
        c.execute('INSERT INTO dashboard_todoitem (id, day_id, todo_item, start_time, end_time) VALUES (?, ?, ?, ?, ?)',
                  (line_recent_primary_key, day, todo_item, start_time, end_time))
        conn.commit()
