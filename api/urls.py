# -*- coding: utf-8 -*-
"""
Url cofigurations
"""
from django.conf.urls import url
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from api.views import book
from api.views import book_format
from api.views import game
from api.views import publisher
from api.views import schema
from api.views import views
from api.views import user_group

router = routers.DefaultRouter()
router.register(r'users', user_group.UserViewSet)
router.register(r'groups', user_group.GroupViewSet)

api_urlpatterns = [ #pylint: disable=invalid-name

    # Book paths
    path('book/<str:id>/<str:edition_id>',
         book.ItemVersionView.as_view(), name="book_edition"),
    path('book/<str:id>', book.ItemView.as_view(), name="book"),
    path('book', book.CreateView.as_view(), name="book_create"),
    path('book', book.ListView.as_view(), name="book_list"),

    # BookFormat paths
    path('book-format/<str:id>', book_format.ItemView.as_view(), name="book_format"),
    path('book-format', book_format.CreateView.as_view(), name="book_format_create"),
    path('book-format', book_format.ListView.as_view(), name="book_format_list"),

    # Game paths
    path('game/<str:id>/<str:version>',
         game.ItemVersionView.as_view(), name="game_version"),
    path('game/<str:id>', game.ItemView.as_view(), name="game"),
    path('game', game.CreateView.as_view(), name="game_create"),
    path('game', game.ListView.as_view(), name="game_list"),

    # Publisher paths
    path('publisher/<str:id>', publisher.ItemView.as_view(), name="publisher"),
    path('publisher', publisher.CreateView.as_view(), name="publisher_create"),
    path('publisher', publisher.ListView.as_view(), name="publisher_list"),

    # Schema paths
    path('schema/<str:id>/<int:version>',
         schema.ItemVersionView.as_view(), name="schema_version"),
    path('schema/<str:id>/<int:version>.json',
         schema.DocumentVersionView.as_view(), name="schema_item_version_json"),
    path('schema/<str:id>', schema.ItemView.as_view(), name="schema"),
    path('schema', schema.CreateView.as_view(), name="schema_create"),
    path('schema', schema.ListView.as_view(), name="schema_list"),

    # system paths
    path('token', views.TokenView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('token/refresh/?', TokenVerifyView.as_view(), name="token_verify"),
    url(r'info/?', views.Root.as_view(), name='info'),
    url(r'^$', RedirectView.as_view(url='info')),

    
    path('', include(router.urls)),
]

schema_view = get_swagger_view( #pylint: disable=invalid-name
    title='RPG Tools API Documentation',
    patterns=api_urlpatterns,
    url="/api/v1/"
)

urlpatterns = api_urlpatterns + [ #pylint: disable=invalid-name
    url(r'docs/', schema_view)
]
