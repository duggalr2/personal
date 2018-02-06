from django import forms
from django.forms import ModelForm
from dashboard.models import Book, Project, Course, Day
from datetime import datetime
from pytz import timezone


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'book_author']


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_description']


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']

DAY_CHOICES = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)


class ReminderForm(forms.Form):
    day = forms.ChoiceField(choices=DAY_CHOICES)
    todo_item = forms.CharField(max_length=2000)
    now_time = timezone('US/Eastern')
    sa_time = datetime.now(now_time)
    # time = forms.TimeField(widget=forms.TextInput(attrs={'placeholder': '4:30 pm'}))
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'),)
