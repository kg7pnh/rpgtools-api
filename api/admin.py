# -*- coding: utf-8 -*-
# TODO: update docstring
"""
Registers modesl for the admin section
"""
from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget
from api.models.book import Book
from api.models.book_format import BookFormat
from api.models.contributor import Contributor
from api.models.game import Game
from api.models.game_system import GameSystem
from api.models.organization import Organization
from api.models.person import Person
from api.models.publisher import Publisher
from api.models.workflow import Workflow


class BookAdmin(admin.ModelAdmin):
    # TODO: update docstring
    """_summary_

    Args:
        admin (_type_): _description_
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
              'publication_year',
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
    # TODO: update docstring
    """_summary_

    Args:
        admin (_type_): _description_
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
    # TODO: update docstring
    """_summary_

    Args:
        admin (_type_): _description_
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
    # TODO: update docstring
    """_summary_

    Args:
        admin (_type_): _description_
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
    # TODO: update docstring
    """_summary_

    Args:
        admin (_type_): _description_
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


class OrganizationAdmin(admin.ModelAdmin):
    # TODO: update docstring
    """_summary_

    Args:
        admin (_type_): _description_
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'name',
              'abbreviation',
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
    # TODO: update docstring
    """_summary_

    Args:
        admin (_type_): _description_
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
    # TODO: update docstring
    """_summary_

    Args:
        admin (_type_): _description_
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


class WorkflowAdmin(admin.ModelAdmin):
    # TODO: update docstring
    """_summary_

    Args:
        admin (_type_): _description_
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget, }
    }
    fields = ('_id',
              'id',
              'created',
              'modified',
              'name',
              'game',
              'workflow_method',
              'definition')
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('name',
                    'created',
                    'modified',
                    'id',
                    '_id')


admin.site.register(Workflow, WorkflowAdmin)
