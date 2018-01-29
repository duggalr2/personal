from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import ast
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.views.generic.list import ListView
from .models import Book, Project, Course
from .forms import CourseForm, ProjectForm, BookForm
from multi_form_view import MultiModelFormView
from django.views.generic import UpdateView, CreateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404



class Home(TemplateView):
    context_object_name = 'home_list'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['book'] = Book.objects.all()
        context['course'] = Course.objects.all()
        context['project'] = Project.objects.all()
        return context


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

