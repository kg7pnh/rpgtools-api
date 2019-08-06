# -*- coding: utf-8 -*-
"""
Url cofigurations
"""
from django.conf import settings
from django.conf.urls import url
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from api.views import book
from api.views import book_format
from api.views import contributor
from api.views import die_roll
from api.views import game
from api.views import game_system
from api.views import organization
from api.views import person
from api.views import publisher
from api.views import schema
from api.views import views
from api.views import user_group

ROUTER = routers.DefaultRouter()
ROUTER.register(r'users', user_group.UserViewSet)
ROUTER.register(r'groups', user_group.GroupViewSet)

api_urlpatterns = [ #pylint: disable=invalid-name

    # Book paths
    path('book/<str:id>', book.ItemView.as_view(), name="book"),
    path('book/', book.CreateView.as_view(), name="book_create"),
    path('book', book.ListView.as_view(), name="book_list"),

    # BookFormat paths
    path('book-format/<str:id>', book_format.ItemView.as_view(), name="book_format"),
    path('book-format/', book_format.CreateView.as_view(), name="book_format_create"),
    path('book-format', book_format.ListView.as_view(), name="book_format_list"),

    # Contributor paths
    path('contributor/<str:id>', contributor.ItemView.as_view(), name="contributor"),
    path('contributor', contributor.ListView.as_view(), name="contributor_list"),

    # DieRoll paths
    path('die-roll', die_roll.DieRollRequest.as_view(), name='die-roll'),

    # Game paths
    path('game/<str:id>', game.ItemView.as_view(), name="game"),
    path('game/', game.CreateView.as_view(), name="game_create"),
    path('game', game.ListView.as_view(), name="game_list"),

    # GameSystem paths
    path('game-system/<str:id>', game_system.ItemView.as_view(), name="game_system"),
    path('game-system/', game_system.CreateView.as_view(), name="game_system_create"),
    path('game-system', game_system.ListView.as_view(), name="game_system_list"),

    # Person paths
    path('organization/<str:id>', organization.ItemView.as_view(), name="organization"),
    path('organization/', organization.CreateView.as_view(), name="organization_create"),
    path('organization', organization.ListView.as_view(), name="organization_list"),

    # Person paths
    path('person/<str:id>', person.ItemView.as_view(), name="person"),
    path('person/', person.CreateView.as_view(), name="person_create"),
    path('person', person.ListView.as_view(), name="person_list"),

    # Publisher paths
    path('publisher/<str:id>', publisher.ItemView.as_view(), name="publisher"),
    path('publisher/', publisher.CreateView.as_view(), name="publisher_create"),
    path('publisher', publisher.ListView.as_view(), name="publisher_list"),

    # Schema paths
    path('schema/<str:id>/<int:version>',
         schema.ItemVersionView.as_view(), name="schema_version"),
    path('schema/<str:id>/<int:version>.json',
         schema.DocumentVersionView.as_view(), name="schema_item_version_json"),
    path('schema/<str:id>', schema.ItemView.as_view(), name="schema"),
    path('schema/', schema.CreateView.as_view(), name="schema_create"),
    path('schema', schema.ListView.as_view(), name="schema_list"),

    # system paths
    path('token', views.TokenView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('token/refresh/?', TokenVerifyView.as_view(), name="token_verify"),
    url(r'info/?', views.Root.as_view(), name='info'),
    url(r'^$', RedirectView.as_view(url='info')),

    path('', include(ROUTER.urls)),
]

urlpatterns = api_urlpatterns + [ #pylint: disable=invalid-name
    url(r'docs/', views.schema_view)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
