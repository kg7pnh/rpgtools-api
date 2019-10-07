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
    path('actions/edit/<str:id>', action.ItemEditView.as_view(), name="action-edit"),
    path('actions/delete/<str:id>', action.ItemDeleteView.as_view(), name="action-delete"),
    path('actions/', action.CreateView.as_view(), name="action-create"),
    path('actions', action.ListView.as_view(), name="action-list"),

    # Action Runner paths
    path('action-runner', action_runner.ActionRunnerRequest.as_view(), name='action-runner'),

    # Book paths
    path('books/<str:id>', book.ItemView.as_view(), name="book-detail"),
    path('books/edit/<str:id>', book.ItemEditView.as_view(), name="book-edit"),
    path('books/delete/<str:id>', book.ItemDeleteView.as_view(), name="book-delete"),
    path('books/', book.CreateView.as_view(), name="book-create"),
    path('books', book.ListView.as_view(), name="book-list"),
    path('books/<str:id>/history', book.BookHistoryView.as_view(), name="book-history"),

    # BookFormat paths
    path('bookformats/<str:id>', book_format.ItemView.as_view(), name="bookformat-detail"),
    path('bookformats/edit/<str:id>', book_format.ItemEditView.as_view(), name="bookformat-edit"),
    path('bookformats/delete/<str:id>', book_format.ItemDeleteView.as_view(), name="bookformat-delete"),
    path('bookformats/', book_format.CreateView.as_view(), name="bookformat-create"),
    path('bookformats', book_format.ListView.as_view(), name="bookformat-list"),

    # Contributor paths
    path('contributors/<str:id>', contributor.ItemView.as_view(), name="contributor-detail"),
    path('contributors', contributor.ListView.as_view(), name="contributor-list"),

    # Die Roll paths
    path('die-roll', die_roll.DieRollRequest.as_view(), name='die-roll'),
    
    # Game paths
    path('games/<str:id>', game.ItemView.as_view(), name="game-detail"),
    path('games/edit/<str:id>', game.ItemEditView.as_view(), name="game-edit"),
    path('games/delete/<str:id>', game.ItemDeleteView.as_view(), name="game-delete"),
    path('games/', game.CreateView.as_view(), name="game-create"),
    path('games', game.ListView.as_view(), name="game-list"),

    # GameSystem paths
    path('gamesystems/<str:id>', game_system.ItemView.as_view(), name="gamesystem-detail"),
    path('gamesystems/edit/<str:id>', game_system.ItemEditView.as_view(), name="gamesystem-edit"),
    path('gamesystems/delete/<str:id>', game_system.ItemDeleteView.as_view(), name="gamesystem-delete"),
    path('gamesystems/', game_system.CreateView.as_view(), name="gamesystem-create"),
    path('gamesystems', game_system.ListView.as_view(), name="gamesystem-list"),

    # Handler paths
    path('handlers/<str:id>', handler.ItemView.as_view(), name="handler-detail"),
    path('handlers/edit/<str:id>', handler.ItemEditView.as_view(), name="handler-edit"),
    path('handlers/delete/<str:id>', handler.ItemDeleteView.as_view(), name="handler-delete"),
    path('handlers/', handler.CreateView.as_view(), name="handler-create"),
    path('handlers', handler.ListView.as_view(), name="handler-list"),

    # Organization paths
    path('organizations/<str:id>', organization.ItemView.as_view(), name="organization-detail"),
    path('organizations/edit/<str:id>', organization.ItemEditView.as_view(), name="organization-edit"),
    path('organizations/delete/<str:id>', organization.ItemDeleteView.as_view(), name="organization-delete"),
    path('organizations/', organization.CreateView.as_view(), name="organization-create"),
    path('organizations', organization.ListView.as_view(), name="organization-list"),

    # Person paths
    path('persons/<str:id>', person.ItemView.as_view(), name="person-detail"),
    path('persons/edit/<str:id>', person.ItemEditView.as_view(), name="person-edit"),
    path('persons/delete/<str:id>', person.ItemDeleteView.as_view(), name="person-delete"),
    path('persons/', person.CreateView.as_view(), name="person-create"),
    path('persons', person.ListView.as_view(), name="person-list"),

    # Publisher paths
    path('publishers/<str:id>', publisher.ItemView.as_view(), name="publisher-detail"),
    path('publishers/edit/<str:id>', publisher.ItemEditView.as_view(), name="publisher-edit"),
    path('publishers/delete/<str:id>', publisher.ItemDeleteView.as_view(), name="publisher-delete"),
    path('publishers/', publisher.CreateView.as_view(), name="publisher-create"),
    path('publishers', publisher.ListView.as_view(), name="publisher-list"),

    # Schema paths
    path('schemas/<str:id>/<int:version>',
         schema.ItemVersionView.as_view(), name="schema-version"),
    path('schemas/<str:id>/<int:version>.json',
         schema.DocumentVersionView.as_view(), name="schema-item-version-json"),
    path('schemas/<str:id>', schema.ItemView.as_view(), name="schema-detail"),
    path('schemas/', schema.CreateView.as_view(), name="schema-create"),
    path('schemas', schema.ListView.as_view(), name="schema-list"),

    # Workflow paths
    path('workflows/<str:id>', workflow.ItemView.as_view(), name="workflow-detail"),
    path('workflows/edit/<str:id>', workflow.ItemEditView.as_view(), name="workflow-edit"),
    path('workflows/delete/<str:id>', workflow.ItemDeleteView.as_view(), name="workflow-delete"),
    path('workflows/', workflow.CreateView.as_view(), name="workflow-create"),
    path('workflows', workflow.ListView.as_view(), name="workflow-list"),

    # system paths
    path('token', views.TokenView.as_view(), name="token-obtain-pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token-refresh"),
    path('token/refresh/?', TokenVerifyView.as_view(), name="token-verify"),
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
