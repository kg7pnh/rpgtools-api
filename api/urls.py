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
from api.views import CurrentUser
from api.views import die_roll
from api.views import game
from api.views import game_system
from api.views import IsAdminView
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

    url(r'current-user/?$', CurrentUser.as_view(), name='user'),
    url(r'is-admin/?$', IsAdminView.as_view(), name='is-admin'),

    # Action paths
    path('actions/<str:id>', action.ItemView.as_view(), name="action"),
    path('actions/edit/<str:id>', action.ItemEditView.as_view(), name="action_edit"),
    path('actions/delete/<str:id>', action.ItemDeleteView.as_view(), name="action_delete"),
    path('actions/', action.CreateView.as_view(), name="action_create"),
    path('actions', action.ListView.as_view(), name="action_list"),

    # Action Runner paths
    path('action-runner', action_runner.ActionRunnerRequest.as_view(), name='action-runner'),

    # Book paths
    path('books/<str:id>', book.ItemView.as_view(), name="book"),
    path('books/edit/<str:id>', book.ItemEditView.as_view(), name="book_edit"),
    path('books/delete/<str:id>', book.ItemDeleteView.as_view(), name="book_delete"),
    path('books/', book.CreateView.as_view(), name="book_create"),
    path('books', book.ListView.as_view(), name="book_list"),

    # BookFormat paths
    path('book-formats/<str:id>', book_format.ItemView.as_view(), name="book_format"),
    path('book-formats/edit/<str:id>', book_format.ItemEditView.as_view(), name="book_format_edit"),
    path('book-formats/delete/<str:id>', book_format.ItemDeleteView.as_view(), name="book_format_delete"),
    path('book-formats/', book_format.CreateView.as_view(), name="book_format_create"),
    path('book-formats', book_format.ListView.as_view(), name="book_format_list"),

    # Contributor paths
    path('contributors/<str:id>', contributor.ItemView.as_view(), name="contributor"),
    path('contributors', contributor.ListView.as_view(), name="contributor_list"),

    # Die Roll paths
    path('die-roll', die_roll.DieRollRequest.as_view(), name='die-roll'),
    
    # Game paths
    path('games/<str:id>', game.ItemView.as_view(), name="game"),
    path('games/edit/<str:id>', game.ItemEditView.as_view(), name="game_edit"),
    path('games/delete/<str:id>', game.ItemDeleteView.as_view(), name="game_delete"),
    path('games/', game.CreateView.as_view(), name="game_create"),
    path('games', game.ListView.as_view(), name="game_list"),

    # GameSystem paths
    path('game-systems/<str:id>', game_system.ItemView.as_view(), name="game_system"),
    path('game-systems/edit/<str:id>', game_system.ItemEditView.as_view(), name="game_system_edit"),
    path('game-systems/delete/<str:id>', game_system.ItemDeleteView.as_view(), name="game_system_delete"),
    path('game-systems/', game_system.CreateView.as_view(), name="game_system_create"),
    path('game-systems', game_system.ListView.as_view(), name="game_system_list"),

    # Handler paths
    path('handlers/<str:id>', handler.ItemView.as_view(), name="handler"),
    path('handlers/edit/<str:id>', handler.ItemEditView.as_view(), name="handler_edit"),
    path('handlers/delete/<str:id>', handler.ItemDeleteView.as_view(), name="handler_delete"),
    path('handlers/', handler.CreateView.as_view(), name="handler_create"),
    path('handlers', handler.ListView.as_view(), name="handler_list"),

    # Organization paths
    path('organizations/<str:id>', organization.ItemView.as_view(), name="organization"),
    path('organizations/edit/<str:id>', organization.ItemEditView.as_view(), name="organization_edit"),
    path('organizations/delete/<str:id>', organization.ItemDeleteView.as_view(), name="organization_delete"),
    path('organizations/', organization.CreateView.as_view(), name="organization_create"),
    path('organizations', organization.ListView.as_view(), name="organization_list"),

    # Person paths
    path('persons/<str:id>', person.ItemView.as_view(), name="person"),
    path('persons/edit/<str:id>', person.ItemEditView.as_view(), name="person_edit"),
    path('persons/delete/<str:id>', person.ItemDeleteView.as_view(), name="person_delete"),
    path('persons/', person.CreateView.as_view(), name="person_create"),
    path('persons', person.ListView.as_view(), name="person_list"),

    # Publisher paths
    path('publishers/<str:id>', publisher.ItemView.as_view(), name="publisher"),
    path('publishers/edit/<str:id>', publisher.ItemEditView.as_view(), name="publisher_edit"),
    path('publishers/delete/<str:id>', publisher.ItemDeleteView.as_view(), name="publisher_delete"),
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
    path('workflows/edit/<str:id>', workflow.ItemEditView.as_view(), name="workflow_edit"),
    path('workflows/delete/<str:id>', workflow.ItemDeleteView.as_view(), name="workflow_delete"),
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
    url(r'^', RedirectView.as_view(url='info')),

    path('', include(ROUTER.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
