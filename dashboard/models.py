from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=500)
    book_author = models.CharField(max_length=1000, default='Kyrie Irving')


class Project(models.Model):
    project_name = models.CharField(max_length=500)
    project_description = models.TextField(blank=True)


class Course(models.Model):
    course_name = models.CharField(max_length=500)


# class Schedule(models.Model):
#     full_day = models.CharField(max_length=500)

