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
from api.views import action
from api.views import action_runner
from api.views import book
from api.views import book_format
from api.views import contributor
from api.views import die_roll
from api.views import game
from api.views import game_system
from api.views import handler
from api.views import organization
from api.views import person
from api.views import publisher
from api.views import schema
from api.views import user_group
from api.views import views
from api.views import workflow

ROUTER = routers.DefaultRouter()
ROUTER.register(r'users', user_group.UserViewSet)
ROUTER.register(r'groups', user_group.GroupViewSet)

api_urlpatterns = [ #pylint: disable=invalid-name

    # Action paths
    path('actions/<str:id>', action.ItemView.as_view(), name="action"),
    path('actions/', action.CreateView.as_view(), name="action_create"),
    path('actions', action.ListView.as_view(), name="action_list"),

    # Action Runner paths
    path('action-runner', action_runner.ActionRunnerRequest.as_view(), name='action-runner'),

    # Book paths
    path('books/<str:id>', book.ItemView.as_view(), name="book"),
    path('books/', book.CreateView.as_view(), name="book_create"),
    path('books', book.ListView.as_view(), name="book_list"),

    # BookFormat paths
    path('book-formats/<str:id>', book_format.ItemView.as_view(), name="book_format"),
    path('book-formats/', book_format.CreateView.as_view(), name="book_format_create"),
    path('book-formats', book_format.ListView.as_view(), name="book_format_list"),

    # Contributor paths
    path('contributors/<str:id>', contributor.ItemView.as_view(), name="contributor"),
    path('contributors', contributor.ListView.as_view(), name="contributor_list"),

    # Die Roll paths
    path('die-roll', die_roll.DieRollRequest.as_view(), name='die-roll'),

    # Game paths
    path('games/<str:id>', game.ItemView.as_view(), name="game"),
    path('games/', game.CreateView.as_view(), name="game_create"),
    path('games', game.ListView.as_view(), name="game_list"),

    # GameSystem paths
    path('game-systems/<str:id>', game_system.ItemView.as_view(), name="game_system"),
    path('game-systems/', game_system.CreateView.as_view(), name="game_system_create"),
    path('game-systems', game_system.ListView.as_view(), name="game_system_list"),

    # Game paths
    path('handlers/<str:id>', handler.ItemView.as_view(), name="handler"),
    path('handlers/', handler.CreateView.as_view(), name="handler_create"),
    path('handlers', handler.ListView.as_view(), name="handler_list"),

    # Organization paths
    path('organizations/<str:id>', organization.ItemView.as_view(), name="organization"),
    path('organizations/', organization.CreateView.as_view(), name="organization_create"),
    path('organizations', organization.ListView.as_view(), name="organization_list"),

    # Person paths
    path('persons/<str:id>', person.ItemView.as_view(), name="person"),
    path('persons/', person.CreateView.as_view(), name="person_create"),
    path('persons', person.ListView.as_view(), name="person_list"),

    # Publisher paths
    path('publishers/<str:id>', publisher.ItemView.as_view(), name="publisher"),
    path('publishers/', publisher.CreateView.as_view(), name="publisher_create"),
    path('publishers', publisher.ListView.as_view(), name="publisher_list"),

    # Schema paths
    path('schemas/<str:id>/<int:version>',
         schema.ItemVersionView.as_view(), name="schema_version"),
    path('schemas/<str:id>/<int:version>.json',
         schema.DocumentVersionView.as_view(), name="schema_item_version_json"),
    path('schemas/<str:id>', schema.ItemView.as_view(), name="schema"),
    path('schemas/', schema.CreateView.as_view(), name="schema_create"),
    path('schemas', schema.ListView.as_view(), name="schema_list"),

    # Workflow paths
    path('workflows/<str:id>', workflow.ItemView.as_view(), name="workflow"),
    path('workflows/', workflow.CreateView.as_view(), name="workflow_create"),
    path('workflows', workflow.ListView.as_view(), name="workflow_list"),

    # system paths
    path('token', views.TokenView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('token/refresh/?', TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns = api_urlpatterns + [ #pylint: disable=invalid-name
    url(r'docs/', views.schema_view),
    url(r'info/?', views.Root.as_view(), name='info'),
    url(r'^$', RedirectView.as_view(url='info')),

    path('', include(ROUTER.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
