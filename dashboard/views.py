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
from .models import Book, Project, Course, FeedDetail, Tweet
from .forms import CourseForm, ProjectForm, BookForm
from django.views.generic import UpdateView, CreateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404
from .scripts import rss_feed, tweet_feed


class Home(TemplateView):
    context_object_name = 'home_list'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['book'] = Book.objects.all()
        context['course'] = Course.objects.all()
        context['project'] = Project.objects.all()
        context['rss_feed'] = FeedDetail.objects.all()[:10]
        context['tweet_feed'] = Tweet.objects.all()[:10]
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
