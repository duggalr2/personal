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
# from .forms import CourseForm, ProjectForm, BookForm
from multi_form_view import MultiModelFormView
from django.views.generic import UpdateView, CreateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy


def home(request):
    return render(request, 'home.html')


class BookCreate(CreateView):
    model = Book
    fields = ['book_name']



# class Home(CreateView):
#     model = Book
#     form_class = BookForm
#     fields = ['book_name']
#     # context_object_name = 'object'
#     template_name = 'Home.html'


    # context_object_name = 'home_list'
    # template_name = 'home.html'


    # form_class = BookForm
    # second_form_class = ProjectForm
    # success_url = reverse_lazy('success')
    #
    # def get_context_data(self, **kwargs):
    #     context = super(AccountProfilesView, self).get_context_data(**kwargs)
    #     user = self.request.user



    # class AccountProfilesView(LoginRequiredMixin, UpdateView):
    #     # All users can access this view
    #     model = get_user_model()
    #     template_name = 'accounts/profile_form.html'
    #     fields = '__all__'
    #
    #     def get_context_data(self, **kwargs):
    #         context = super(AccountProfilesView, self).get_context_data(**kwargs)
    #         user = self.request.user
    #
    #         if not self.request.POST:
    #             if user.is_student:
    #                 profile = user.get_student_profile()
    #                 context['userprofile'] = profile
    #                 context['form_student'] = forms.StudentProfileForm()
    #             elif user.is_professor:
    #                 profile = user.get_professor_profile()
    #                 context['userprofile'] = profile
    #                 context['form_professor'] = forms.ProfessorProfileForm()
    #             elif user.is_executive:
    #                 profile = user.get_executive_profile()
    #                 context['userprofile'] = profile
    #                 context['form_executive'] = forms.ExecutiveProfileForm()
    #             elif user.is_student and user.is_professor and user.is_executive:
    #                 student_profile = user.get_student_profile()
    #                 professor_profile = user.get_professor_profile()
    #                 executive_profile = user.get_executive_profile()
    #
    #                 context['student_profile'] = student_profile
    #                 context['professor_profile'] = professor_profile
    #                 context['executive_profile'] = executive_profile
    #
    #                 context['form_student'] = forms.StudentProfileForm()
    #                 context['form_professor'] = forms.ProfessorProfileForm()
    #                 context['form_executive'] = forms.ExecutiveProfileForm()
    #
    #         return context
    #
    #     def post(self, request, *args, **kwargs):
    #         self.object = self.get_object()
    #         user = self.request.user
    #         if user.is_student:
    #             context['form_student'] = forms.StudentProfileForm(self.request.POST)
    #         elif user.is_professor:
    #             context['form_professor'] = forms.ProfessorProfileForm(self.request.POST)
    #         elif user.is_executive:
    #             context['form_executive'] = forms.ExecutiveProfileForm(self.request.POST)
    #         elif user.is_student and user.is_professor and user.is_executive:
    #             context['form_student'] = forms.StudentProfileForm(self.request.POST)
    #             context['form_professor'] = forms.ProfessorProfileForm(self.request.POST)
    #             context['form_executive'] = forms.ExecutiveProfileForm(self.request.POST)
    #
    #         return super(AccountProfilesView, self).post(request, *args, **kwargs)
    #
    #     def form_valid(self, form):
    #         context = self.get_context_data(form=form)
    #         user = self.request.user
    #         user = form.save()
    #         if user.is_student:
    #             student = context['form_student'].save(commit=False)
    #             student.user = user
    #             student.save()
    #         elif user.is_professor:
    #             professor = context['form_professor'].save(commit=False)
    #             professor.user = user
    #             professor.save()
    #         elif user.is_executive:
    #             executive = context['form_executive'].save(commit=False)
    #             executive.user = user
    #             executive.save()
    #         elif user.is_student and user.is_professor and user.is_executive:
    #             student = context['form_student'].save(commit=False)
    #             student.user = user
    #             student.save()
    #             professor = context['form_professor'].save(commit=False)
    #             professor.user = user
    #             professor.save()
    #             executive = context['form_executive'].save(commit=False)
    #             executive.user = user
    #             executive.save()
    #
    #         return super(AccountProfilesView, self).form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super(Home, self).get_context_data(**kwargs)
#         if 'form' not in context:
#             context['form'] = self.form_class(initial={'some_field': context['model'].some_field})
#         if 'form2' not in context:
#             context['form2'] = self.second_form_class(initial={'another_field': context['model'].another_field})
#         return context
#         # context = super(Home, self).get_context_data(**kwargs)
#         # context['book'] = Book.objects.all()
#         # context['course'] = Course.objects.all()
#         # return context
#
#     def get_object(self):
#         return get_object_or_404(Model, pk=self.request.session['someval'])
#
#     def form_invalid(self, **kwargs):
#         return self.render_to_response(self.get_context_data(**kwargs))
#
#     def post(self, request, *args, **kwargs):
#
#         # get the user instance
#         self.object = self.get_object()
#
#         # determine which form is being submitted
#         # uses the name of the form's submit button
#         if 'form' in request.POST:
#
#             # get the primary form
#             form_class = self.get_form_class()
#             form_name = 'form'
#
#         else:
#
#             # get the secondary form
#             form_class = self.second_form_class
#             form_name = 'form2'
#
#         # get the form
#         form = self.get_form(form_class)
#
#         # validate
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(**{form_name: form})
#
#
#     #
#     # def book_form_valid(self, form):
#     #     book = form.save(self.request)
#     #     return form.book(self.request, book, self.get_success_url())
#
#
# # class MyView(UpdateView):
# #
# #     template_name = 'template.html'
# #     form_class = Form1
# #     second_form_class = Form2
# #     success_url = reverse_lazy('success')
# #
# #     def get_context_data(self, **kwargs):
# #         context = super(MyView, self).get_context_data(**kwargs)
# #         if 'form' not in context:
# #             context['form'] = self.form_class(initial={'some_field': context['model'].some_field})
# #         if 'form2' not in context:
# #             context['form2'] = self.second_form_class(initial={'another_field': context['model'].another_field})
# #         return context
# #
# #     def get_object(self):
# #         return get_object_or_404(Model, pk=self.request.session['someval'])
# #
# #     def form_invalid(self, **kwargs):
# #         return self.render_to_response(self.get_context_data(**kwargs))
# #
# #     def post(self, request, *args, **kwargs):
# #
# #         # get the user instance
# #         self.object = self.get_object()
# #
# #         # determine which form is being submitted
# #         # uses the name of the form's submit button
# #         if 'form' in request.POST:
# #
# #             # get the primary form
# #             form_class = self.get_form_class()
# #             form_name = 'form'
# #
# #         else:
# #
# #             # get the secondary form
# #             form_class = self.second_form_class
# #             form_name = 'form2'
# #
# #         # get the form
# #         form = self.get_form(form_class)
# #
# #         # validate
# #         if form.is_valid():
# #             return self.form_valid(form)
# #         else:
# #             return self.form_invalid(**{form_name: form})
#
#
#
# # class SignupLoginView(MultiFormsView):
# #     template_name = 'public/my_login_signup_template.html'
# #     form_classes = {'login': LoginForm,
# #                     'signup': SignupForm}
# #     success_url = 'my/success/url'
# #
# #     def get_login_initial(self):
# #         return {'email':'dave@dave.com'}
# #
# #     def get_signup_initial(self):
# #         return {'email':'dave@dave.com'}
# #
# #     def get_context_data(self, **kwargs):
# #         context = super(SignupLoginView, self).get_context_data(**kwargs)
# #         context.update({"some_context_value": 'blah blah blah',
# #                         "some_other_context_value": 'blah'})
# #         return context
# #
# #     def login_form_valid(self, form):
# #         return form.login(self.request, redirect_url=self.get_success_url())
# #
# #     def signup_form_valid(self, form):
# #         user = form.save(self.request)
# #         return form.signup(self.request, user, self.get_success_url())