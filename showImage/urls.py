from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
urlpatterns = [

    re_path(r'',TemplateView.as_view(template_name="showImage/test.html"),name='test'),
]
