# -*- coding: utf-8 -*-
"""
Url cofigurations
"""
from django.conf import settings
from django.conf.urls import url
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from api.views import action_runner
from api.views import book
from api.views import book_format
from api.views import contributor
from api.views import CurrentUser
from api.views import die_roll
from api.views import game
from api.views import game_system
from api.views import IsAdminView
from api.views import organization
from api.views import person
from api.views import publisher
from api.views import user_group
from api.views import views
from api.views import workflow

ROUTER = routers.DefaultRouter()
ROUTER.register(r'users', user_group.UserViewSet)
ROUTER.register(r'groups', user_group.GroupViewSet)

schema_view = get_schema_view( # pylint: disable=invalid-name
    openapi.Info(
        title='RPGTools API',
        default_version='v.1.0.0',
        description='API access to tools '+
        'and information for RPG players '+
        'and game masters.',
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)

api_urlpatterns = [ #pylint: disable=invalid-name

    url(r'current-user/?$',
        CurrentUser.as_view(),
        name='user'),
    url(r'is-admin/?$',
        IsAdminView.as_view(),
        name='is_admin'),

    # Action Runner paths
    path('action-runner',
         action_runner.ActionRunnerRequest.as_view(),
         name='action_runner'),

    # Book paths
    path('books/<str:id>',
         book.ItemView.as_view(),
         name="book_detail"),
    path('books/edit/<str:id>',
         book.ItemEditView.as_view(),
         name="book_edit"),
    path('books/delete/<str:id>',
         book.ItemDeleteView.as_view(),
         name="book_delete"),
    path('books/',
         book.CreateView.as_view(),
         name="book_create"),
    path('books',
         book.ListView.as_view(),
         name="book_list"),
    path('books/<str:id>/history',
         book.BookHistoryView.as_view(),
         name="book_history"),

    # BookFormat paths
    path('bookformats/<str:id>',
         book_format.ItemView.as_view(),
         name="bookformat_detail"),
    path('bookformats/edit/<str:id>',
         book_format.ItemEditView.as_view(),
         name="bookformat_edit"),
    path('bookformats/delete/<str:id>',
         book_format.ItemDeleteView.as_view(),
         name="bookformat_delete"),
    path('bookformats/',
         book_format.CreateView.as_view(),
         name="bookformat_create"),
    path('bookformats',
         book_format.ListView.as_view(),
         name="bookformat_list"),
    path('bookformats/<str:id>/history',
         book_format.BookFormatHistoryView.as_view(),
         name="booformatk_history"),

    # Contributor paths
    path('contributors/<str:id>',
         contributor.ItemView.as_view(),
         name="contributor_detail"),
    path('contributors',
         contributor.ListView.as_view(),
         name="contributor_list"),

    # Die Roll paths
    path('die-roll',
         die_roll.DieRollRequest.as_view(),
         name='die_roll'),

    # Game paths
    path('games/<str:id>',
         game.ItemView.as_view(),
         name="game_detail"),
    path('games/edit/<str:id>',
         game.ItemEditView.as_view(),
         name="game_edit"),
    path('games/delete/<str:id>',
         game.ItemDeleteView.as_view(),
         name="game_delete"),
    path('games/',
         game.CreateView.as_view(),
         name="game_create"),
    path('games',
         game.ListView.as_view(),
         name="game_list"),
    path('games/<str:id>/history',
         game.GameHistoryView.as_view(),
         name="game_history"),

    # GameSystem paths
    path('gamesystems/<str:id>',
         game_system.ItemView.as_view(),
         name="gamesystem_detail"),
    path('gamesystems/edit/<str:id>',
         game_system.ItemEditView.as_view(),
         name="gamesystem_edit"),
    path('gamesystems/delete/<str:id>',
         game_system.ItemDeleteView.as_view(),
         name="gamesystem_delete"),
    path('gamesystems/',
         game_system.CreateView.as_view(),
         name="gamesystem_create"),
    path('gamesystems',
         game_system.ListView.as_view(),
         name="gamesystem_list"),
    path('gamesystems/<str:id>/history',
         game_system.GameSystemHistoryView.as_view(),
         name="gamesystem_history"),

    # Organization paths
    path('organizations/<str:id>',
         organization.ItemView.as_view(),
         name="organization_detail"),
    path('organizations/edit/<str:id>',
         organization.ItemEditView.as_view(),
         name="organization_edit"),
    path('organizations/delete/<str:id>',
         organization.ItemDeleteView.as_view(),
         name="organization_delete"),
    path('organizations/',
         organization.CreateView.as_view(),
         name="organization_create"),
    path('organizations',
         organization.ListView.as_view(),
         name="organization_list"),
    path('organizations/<str:id>/history',
         organization.OrganizationHistoryView.as_view(),
         name="organization_history"),

    # Person paths
    path('persons/<str:id>',
         person.ItemView.as_view(),
         name="person_detail"),
    path('persons/edit/<str:id>',
         person.ItemEditView.as_view(),
         name="person_edit"),
    path('persons/delete/<str:id>',
         person.ItemDeleteView.as_view(),
         name="person_delete"),
    path('persons/',
         person.CreateView.as_view(),
         name="person_create"),
    path('persons',
         person.ListView.as_view(),
         name="person_list"),
    path('persons/<str:id>/history',
         person.PersonHistoryView.as_view(),
         name="person_history"),

    # Publisher paths
    path('publishers/<str:id>',
         publisher.ItemView.as_view(),
         name="publisher_detail"),
    path('publishers/edit/<str:id>',
         publisher.ItemEditView.as_view(),
         name="publisher_edit"),
    path('publishers/delete/<str:id>',
         publisher.ItemDeleteView.as_view(),
         name="publisher_delete"),
    path('publishers/',
         publisher.CreateView.as_view(),
         name="publisher_create"),
    path('publishers',
         publisher.ListView.as_view(),
         name="publisher_list"),
    path('publishers/<str:id>/history',
         publisher.PublisherHistoryView.as_view(),
         name="publisher_history"),

    # Workflow paths
    path('workflows/<str:id>',
         workflow.ItemView.as_view(),
         name="workflow_detail"),
    path('workflows/edit/<str:id>',
         workflow.ItemEditView.as_view(),
         name="workflow_edit"),
    path('workflows/delete/<str:id>',
         workflow.ItemDeleteView.as_view(),
         name="workflow_delete"),
    path('workflows/',
         workflow.CreateView.as_view(),
         name="workflow_create"),
    path('workflows',
         workflow.ListView.as_view(),
         name="workflow_list"),

    # system paths
    path('token',
         views.TokenView.as_view(),
         name="token_obtain_pair"),
    path('token/refresh',
         TokenRefreshView.as_view(),
         name="token_refresh"),
    path('token/refresh/',
         TokenVerifyView.as_view(),
         name="token_verify"),
]

urlpatterns = api_urlpatterns + [ #pylint: disable=invalid-name
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    url(r'info/?', views.Root.as_view(), name='info'),
    url(r'^$', RedirectView.as_view(url='info')),
    url(r'^', RedirectView.as_view(url='info')),
    path('', include(ROUTER.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [ # pylint: disable=invalid-name
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
