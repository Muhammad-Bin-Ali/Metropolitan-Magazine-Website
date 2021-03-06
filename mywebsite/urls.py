"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from landing_page import views as landing_page_views
from django.views.generic import TemplateView
from read_later.views import ReadLaterView, ReadLater_Ajax


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include("main_news.urls")),
    path('', landing_page_views.templanding, name = 'landing-page'),
    path('accounts/', include('allauth.urls')),
    path('login/', TemplateView.as_view(template_name='usersbackend/index.html')),
    path('<str:username>/read-later/', ReadLaterView.as_view(), name = 'read-later-page'),
    path('read-later/ajax', ReadLater_Ajax.as_view(), name='ajax-read-later')
]
