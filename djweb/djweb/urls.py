"""djweb URL Configuration

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
from django.urls import path,re_path
from webapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('Ms938reportupload/', views.Ms938reportupload),
    path('Ms648reportupload/', views.Ms648reportupload),
    path('', views.login),
    path('Ms938uploadnew/', views.Ms938uploadnew),
    path('Ms938uploadold/', views.Ms938uploadold),
    path('Ms648uploadnew/', views.Ms648uploadnew),
    path('Ms648uploadold/', views.Ms648uploadold),
    path('ms938report/', views.ms938report),
    path('ms938reportok/', views.ms938reportok),
    path('ms938reportResult/', views.ms938reportResult),
    path('ms648report/', views.ms648report),
    path('ms648reportok/', views.ms648reportok),
    path('ms648reportResult/', views.ms648reportResult),
    path('reportrecord938/',views.reportrecord938),
    path('reportrecord/',views.reportrecord),
    path('record938/',views.record938),
    path('record648/',views.record648),
    path('reportForm/', views.reportForm),
    path('student/', views.student),
    path('st1/', views.st1),
    re_path('StressTestReport_Demeter/.*', views.StressTestReport_Demeter),
    re_path('StressTestReport_Hera/.*', views.StressTestReport_Hera),
]
