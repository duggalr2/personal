from django.db import models
from datetime import datetime


class Book(models.Model):
    book_name = models.CharField(max_length=500)
    book_author = models.CharField(max_length=1000, default='Kyrie Irving')


class Project(models.Model):
    project_name = models.CharField(max_length=500)
    project_description = models.TextField(blank=True)


class Course(models.Model):
    course_name = models.CharField(max_length=500)


class FeedUrl(models.Model):
    url = models.URLField()


class FeedDetail(models.Model):
    feed_url = models.ForeignKey(FeedUrl, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, default='asd')
    story_url = models.URLField(default='https://www.google.ca/')
    timestamp = models.TimeField(default=datetime.now().time())


class Tweet(models.Model):
    tweet = models.CharField(max_length=1000)


class Day(models.Model):
    day = models.CharField(max_length=500)


class TodoItem(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    todo_item = models.CharField(max_length=2000)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Reminder(models.Model):
    # day = models.ForeignKey(Day, on_delete=models.CASCADE)
    day = models.CharField(max_length=1000) # TODO: NEED TO LINK THIS TO ABOVE!
    todo_item = models.CharField(max_length=2000)
    time = models.TimeField(default=datetime.now().time())



# class FeedUrl(models.Model):
#     url = models.URLField(max_length=500)

# class FeedDetail(models.Model):
#     feed_url = models.ForeignKey(FeedUrl, on_delete=models.CASCADE)
#     story_url = models.URLField()
#     story_description = models.TextField()

# class Schedule(models.Model):
#     full_day = models.CharField(max_length=500)

