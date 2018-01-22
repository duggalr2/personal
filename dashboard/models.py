from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=500)


class Project(models.Model):
    project_name = models.CharField(max_length=500)
    project_description = models.TextField()


class Course(models.Model):
    course_name = models.CharField(max_length=500)


# class Schedule(models.Model):
#     book_name = models.CharField(max_length=500)
#
