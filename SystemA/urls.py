"""SystemA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from .service import login_service
from .service import select_service
from .service import drop_service
from .service import get_service
from .service import student_service

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',admin.site.urls),
    url(r'^usrlogin/$', login_service.login),
    url(r'^course/select/$',select_service.select),
    url(r'^course/drop/$',drop_service.drop),
    url(r'^course/getAll/$',get_service.getAll),
    url(r'^course/getStuSelect$',get_service.getStu),
    url(r'^course/getStu/$',get_service.getSelect),
    url(r'^course/getAllSelect/$',get_service.getAllSelect),
    url(r'^course/check/$',get_service.checkSelect),
    url(r'^course/statistic/$',get_service.getStatistic),
    url(r'^student/getAll/$',student_service.getAll),
    url(r'^student/getStu/$',student_service.getStu),
    url(r'^student/addStu/$',student_service.addStu),
    url(r'^index/$',TemplateView.as_view(template_name="index.html"),name="index"),
    url(r'^form/$',TemplateView.as_view(template_name="form.html"),name="form")
]
