# -*- coding: utf-8 -*-
"""
rpgtools URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include
from django.urls import path
from django.urls import reverse_lazy
from django.urls import re_path
from markdownx import urls as markdownx

urlpatterns = [ # pylint: disable=invalid-name
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin/', admin.site.urls),
    path('api/', RedirectView.as_view(url='/api/v1/')),
    re_path('api/v1/', include('api.urls'), name='api'),
    url(r'^markdownx/', include(markdownx)),
]
