"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', 'app.views.register', name='app_register'),
    url(r'^$', 'app.views.homepage', name='app_homepage'),
    url(r'^accounts/login/$', 'app.views.do_login', name='app_login'),
    url(r'^accounts/logout/$', 'app.views.logout', name='app_logout'),
    url(r'^about/', 'app.views.about', name='app_about'),
    url(r'^contact/', 'app.views.contact', name='app_contact'),
    url(r'^blog/$', 'app.views.blog_list', name='blog_index'),
    url(r'^blog/(?P<blog_id>[0-9]+)$', 'app.views.blog_details', name='blog_details')
]
