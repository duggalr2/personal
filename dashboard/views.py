# from django.contrib.auth import login, authenticate
# from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# import ast
# from django.contrib.auth.decorators import user_passes_test
# from django.conf import settings
# from django.views.generic.list import ListView
# from multi_form_view import MultiModelFormView
from django.shortcuts import render, redirect
from .models import Book, Project, Course, FeedDetail, Tweet, TodoItem, Reminder, Day
from .forms import CourseForm, ProjectForm, BookForm, ReminderForm
from django.views.generic import UpdateView, CreateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404
from .scripts import rss_feed, tweet_feed, send_notification, quickstart
from datetime import datetime
from datetime import date
from pytz import timezone
import requests


def update_calendar(request):
    pass


class Home(TemplateView): # TODO: NEED TO THINK OF POSSIBLE ERROR CASES!!!! ***TEST THEM***
    context_object_name = 'home_list'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['book'] = Book.objects.all()
        context['course'] = Course.objects.all()
        context['project'] = Project.objects.all()
        context['rss_feed'] = FeedDetail.objects.all()[:10]
        context['tweet_feed'] = Tweet.objects.all()[:10]
        context['schedule'] = TodoItem.objects.all()
        context['current_day'] = datetime.now().strftime("%A")
        now_time = timezone('US/Eastern')
        sa_time = datetime.now(now_time)
        context['current_time'] = sa_time
        context['reminder'] = Reminder.objects.all()
        new = sa_time.strftime("%H:%M")
        # print(sa_time, type(sa_time))
        # print(new, type(new))
        # print(TodoItem.objects.all()[0].start_time, type(TodoItem.objects.all()[0].start_time))
        d = date.today()
        # y = datetime.combine(d, TodoItem.objects.all()[0].start_time)
        # print(y.replace(tzinfo=None) <= sa_time.replace(tzinfo=None))

        context['current_item'] = None
        if len(TodoItem.objects.all()) > 0:
            for item in TodoItem.objects.all():
                if item.day_id == datetime.now().strftime("%A"):
                    if item.end_time is not None:
                        y = datetime.combine(d, item.start_time)
                        w = datetime.combine(d, item.end_time)
                        if y <= sa_time.replace(tzinfo=None) <= w:
                            context['current_item'] = item
                            # context['current_item_end_time'] = item.end_time

            # Handling the Localstorage Modal
            if context['current_item'] is not None:
                item = context['current_item']
                adjust_end_time = datetime.combine(d, item.end_time)
                print(adjust_end_time, sa_time.replace(tzinfo=None))
                if adjust_end_time < sa_time.replace(tzinfo=None):
                    context['change'] = True
                else:
                    context['change'] = False

        # Job Tracking
        r = requests.get('http://127.0.0.1:8000/profiles/?format=json')
        context['job_track'] = r.json()

        company_list = []
        profiles = {}
        for profile in r.json():
            company_name = profile.get('company_name')
            company_list.append(company_name)
        for num in range(len(company_list)):
            temp_li = []
            for profile in r.json():
                company_name = profile.get('company_name')
                if company_list[num] == company_name:
                    temp_li.append(profile.get('linkedin_url'))
            profiles[company_list[0]] = temp_li
        context['job_track'] = profiles

        # Sending Push Reminder Notifications to my phone
        reminder_objects = Reminder.objects.all().filter(day=datetime.now().strftime("%A"))
        for reminder in reminder_objects:
            if str(reminder.time.strftime("%H:%M")) == str(sa_time.strftime("%H:%M")):
                send_notification.send_notification(reminder.todo_item)
                print('Reminder Notification Sent!')
                reminder.delete()

        # Checking and Changing the Schedule on day-to-day basis
        if len(Day.objects.all()) > 0:
            day_in_db = Day.objects.all()[0].day
            if datetime.now().strftime("%A") != day_in_db:
                Day.objects.all().delete()
                TodoItem.objects.all().delete()
                quickstart.main()
        return context


def feed_refresh(request):
    rss_feed.run_it()
    return redirect('home')


def tweet_refresh(request):
    tweet_feed.execute_tweets()
    return redirect('home')


def book_crete(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'book_form.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('home')


def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'book_form.html', {'form': form})


def project_update(request, pk):
    book = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'book_form.html', {'form': form})


def project_delete(request, pk):
    book = get_object_or_404(Project, pk=pk)
    book.delete()
    return redirect('home')


def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'book_form.html', {'form': form})


def course_update(request, pk):
    book = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'book_form.html', {'form': form})


def course_delete(request, pk):
    book = get_object_or_404(Course, pk=pk)
    book.delete()
    return redirect('home')


def rssFeed(request):
    rss_feed = FeedDetail.objects.all()
    return render(request, 'rss_feed.html', {'rss_feed': rss_feed})


def tweetFeed(request):
    tweet_feed = Tweet.objects.all()
    return render(request, 'tweet_feed.html', {'tweet_feed': tweet_feed})


# TODO: Build remaining portion of reminder form
def reminder_create(request):
    form = ReminderForm(request.POST or None)
    if form.is_valid():
        day = form.cleaned_data.get('day')
        todo_item = form.cleaned_data.get('todo_item')
        time = form.cleaned_data.get('time')
        b = Reminder.objects.create(day=day, todo_item=todo_item, time=time)
        b.save()
        return redirect('home')
    return render(request, 'book_form.html', {'form': form})


def reminder_delete(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    reminder.delete()
    return redirect('home')


def update_session(request):
    request.session['view'] = False

