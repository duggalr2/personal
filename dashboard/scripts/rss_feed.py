from multiprocessing.pool import ThreadPool
import feedparser
import sqlite3
from time import mktime
from datetime import datetime


def parse_feed(feed_url):
    result = []
    parsed_feed = feedparser.parse(feed_url)
    for story in parsed_feed.get('entries'):
        title = story.get('title')
        link = story.get('link')
        last_timestamp = story.get('updated_parsed')
        result.append([title, link, last_timestamp, feed_url])
    return result


conn = sqlite3.connect('/Users/Rahul/Desktop/Side_projects/personal/db.sqlite3', check_same_thread=False)
c = conn.cursor()
c.execute('SELECT url FROM dashboard_feedurl')
url_list = c.fetchall()
hit_list = [url[0] for url in url_list]


def add_url(url):
    c.execute('SELECT MAX(id) FROM dashboard_feedurl')
    recent_primary_key = c.fetchone()
    if recent_primary_key[0] is None:
        recent_primary_key = 1
    else:
        recent_primary_key = recent_primary_key[0]
    c.execute('INSERT INTO dashboard_feedurl (id, url) VALUES (?, ?)', (recent_primary_key+1, url))
    conn.commit()


def feed_execute(parsed_feed):
    c.execute('SELECT MAX(id) FROM dashboard_feeddetail')
    recent_primary_key = c.fetchone()
    if recent_primary_key[0] is None:
        recent_primary_key = 1
    else:
        recent_primary_key = recent_primary_key[0]

    for number in range(len(parsed_feed)):
        recent_primary_key += 1
        title = parsed_feed[number][0]
        link = parsed_feed[number][1]
        struct = parsed_feed[number][2]
        dt = datetime.fromtimestamp(mktime(struct))
        time = dt.strftime('%H:%M:%S')
        feed_url = parsed_feed[number][-1]
        c.execute("INSERT INTO dashboard_feeddetail (id, feed_url_id, title, story_url, timestamp) VALUES (?, ?, ?, ?, ?)",
                  (recent_primary_key, feed_url, title, link, time))
        conn.commit()
    print('RSS Done')


def run_it():
    """ Main function used in Django view to fetch all rss feeds"""
    c.execute("DELETE FROM dashboard_feeddetail")
    conn.commit()
    pool = ThreadPool()
    results = pool.map(parse_feed, hit_list)
    for result in results:
        feed_execute(result)



