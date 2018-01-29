from django.forms import ModelForm
from dashboard.models import Book, Project, Course


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

