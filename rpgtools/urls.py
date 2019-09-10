"""rpgtools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView

from django.urls import include
from django.urls import path
from django.urls import reverse_lazy
from django.urls import re_path

from markdownx import urls as markdownx

# import api.urls

urlpatterns = [ # pylint: disable=invalid-name
    # url(r'^$', RedirectView.as_view(url='admin/')),
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin/', admin.site.urls), 
    path('api/', RedirectView.as_view(url='/api/v1/')),
    re_path('api/v1/', include('api.urls'), name='api'),
    url(r'^markdownx/', include(markdownx)),
]
