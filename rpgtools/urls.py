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
from django.conf import settings
# from django.conf.urls import include
# from django.conf.urls import path
# from django.conf.urls import re_path
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.static import serve
from markdownx import urls as markdownx

# import api.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(loginapp.urls)),
    # path('', include(catalogweb.urls)),
    # path('ui/', include(omf_ui.urls)),
    # url(r'^markdownx/', include(markdownx)),
    # re_path('api/v1/', include('api.urls')),
]
