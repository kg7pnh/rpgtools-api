# -*- coding: utf-8 -*-
"""
Registers modesl for the admin section
"""
from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget
from api.models.action import Action
from api.models.book import Book
from api.models.book_format import BookFormat
from api.models.contributor import Contributor
from api.models.game import Game
from api.models.game_system import GameSystem
from api.models.handler import Handler
from api.models.organization import Organization
from api.models.person import Person
from api.models.publisher import Publisher
from api.models.schema import Schema
from api.models.workflow import Workflow

# Register your models here.
class ActionAdmin(admin.ModelAdmin):
    """
    ActionAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget,}
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name',
              'game',
              'input_schema',
              'output_schema')
    readonly_fields = ('_id',
                        'id',
                        'created',
                        'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(Action, ActionAdmin)

class BookAdmin(admin.ModelAdmin):
    """
    BookAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name',
              'publisher',
              'game',
              'book_format',
              'short_name',
              'abbreviation',
              'catalog_number',
              'pages',
              'isbn_10',
              'isbn_13',
              'description',
              'read_me',
              'url',
              'art_assistant',
              'art_director',
              'artist_cover',
              'artist_interior',
              'author',
              'designer',
              'developer',
              'editor',
              'graphic_designer',
              'play_tester',
              'proofreader',
              'research_assistant',
              'text_manager',
              'text_processor',
              'type_setter')
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')
    filter_horizontal = ('art_assistant',
                         'art_director',
                         'artist_cover',
                        'artist_interior',
                        'author',
                        'designer',
                        'developer',
                        'editor',
                        'graphic_designer',
                        'play_tester',
                        'proofreader',
                        'research_assistant',
                        'text_manager',
                        'text_processor',
                        'type_setter',)

admin.site.register(Book, BookAdmin)

class BookFormatAdmin(admin.ModelAdmin):
    """
    BookFormatAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name',
              'format_type',
              'description',
              'read_me',
              'url',)
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(BookFormat, BookFormatAdmin)

class ContributorAdmin(admin.ModelAdmin):
    """
    ContributorAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'name',
              'created',
              'modified',
              'description',
              'read_me',
              'url')
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(Contributor, ContributorAdmin)

class GameAdmin(admin.ModelAdmin):
    """
    GameAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name',
              'short_name',
              'abbreviation',
              'publisher',
              'game_system',
              'description',
              'read_me',
              'url')
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(Game, GameAdmin)

class GameSystemAdmin(admin.ModelAdmin):
    """
    GameSystemAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name',
              'short_name',
              'abbreviation',
              'publisher',
              'description',
              'read_me',
              'url')
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(GameSystem, GameSystemAdmin)

class HandlerAdmin(admin.ModelAdmin):
    """
    WorkflowAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget,}
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name',
              'game',
              'method',
              'api_resource')
    readonly_fields = ('_id',
                        'id',
                        'created',
                        'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(Handler, HandlerAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    """
    ContributorAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'name',
              'created',
              'modified',
              'description',
              'read_me',
              'url')
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(Organization, OrganizationAdmin)

class PersonAdmin(admin.ModelAdmin):
    """
    BookAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name_prefix',
              'name_first',
              'name_middle',
              'name_last',
              'name_suffix',
              'description',
              'read_me',
              'url')
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('id',
                    'name_prefix',
                    'name_first',
                    'name_middle',
                    'name_last',
                    'name_suffix',
                    'created',
                    'modified',
                    '_id')

admin.site.register(Person, PersonAdmin)

class PublisherAdmin(admin.ModelAdmin):
    """
    PublisherAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name',
              'abbreviation',
              'description',
              'read_me',
              'url')
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(Publisher, PublisherAdmin)

class SchemaAdmin(admin.ModelAdmin):
    """
    SchemaAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'name',
              'version',
              'created',
              'modified',
              'document',
              'form_schema',
              'specification',
              'description',
              'read_me',
              'url')
    readonly_fields = ('_id',
                       'id',
                       'version',
                       'created',
                       'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(Schema, SchemaAdmin)

class WorkflowAdmin(admin.ModelAdmin):
    """
    WorkflowAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget,}
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name',
              'game',
              'actions')
    readonly_fields = ('_id',
                        'id',
                        'created',
                        'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')
    filter_horizontal = ('actions',)

admin.site.register(Workflow, WorkflowAdmin)
