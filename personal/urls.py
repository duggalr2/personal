"""personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dashboard import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.Home.as_view(), name='home'),
    url(r'^book_create$', views.book_crete, name='book_create'),
    url(r'^book_update/(?P<pk>\d+)$', views.book_update, name='book_update'),
    url(r'^book_delete/(?P<pk>\d+)$', views.book_delete, name='book_delete'),
    url(r'^project_create$', views.project_create, name='project_create'),
    url(r'^project_update/(?P<pk>\d+)$', views.project_update, name='project_update'),
    url(r'^project_delete/(?P<pk>\d+)$', views.project_delete, name='project_delete'),
    url(r'^course_create$', views.course_create, name='course_create'),
    url(r'^course_update/(?P<pk>\d+)$', views.course_update, name='course_update'),
    url(r'^course_delete/(?P<pk>\d+)$', views.course_delete, name='course_delete'),
    url(r'^feed/', views.rssFeed, name='rssFeed'),
    url(r'^feed_refresh/', views.feed_refresh, name='feed_refresh'),
    url(r'^tweet_refresh/', views.tweet_refresh, name='tweet_refresh'),
    url(r'^tweet/', views.tweetFeed, name='tweetFeed'),
    url(r'^reminder_create$', views.reminder_create, name='reminder_create'),
    url(r'^reminder_delete/(?P<pk>\d+)$', views.reminder_delete, name='reminder_delete'),
    url(r'^update_calendar/', views.update_calendar, name='update_calendar'),
]

