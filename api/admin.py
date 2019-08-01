# -*- coding: utf-8 -*-
"""
Registers modesl for the admin section
"""
from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget
from api.models.book import Book
from api.models.book_format import BookFormat
from api.models.game import Game
from api.models.game_system import GameSystem
from api.models.person import Person
from api.models.publisher import Publisher
from api.models.schema import Schema

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    """
    BookAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'name',
              'publisher',
              'game',
              'book_format',
              'short_name',
              'abbreviation',
              'catalog_number',
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
              'type_setter',
              'pages',
              'isbn_10',
              'isbn_13',
              'url',
              'created',
              'modified',
              'description')
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
              'name',
              'format_type',
              'created',
              'modified',
              'description')
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

class GameAdmin(admin.ModelAdmin):
    """
    GameAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'name',
              'short_name',
              'abbreviation',
              'publisher',
              'game_system',
              'url',
              'created',
              'modified',
              'description')
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
              'name',
              'short_name',
              'abbreviation',
              'publisher',
              'url',
              'created',
              'modified',
              'description')
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

class PersonAdmin(admin.ModelAdmin):
    """
    BookAdmin
    """
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fields = ('_id',
              'id',
              'name_prefix',
              'name_first',
              'name_middle',
              'name_last',
              'name_suffix',
              'created',
              'modified',
              'description')
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
              'name',
              'abbreviation',
              'url',
              'created',
              'modified',
              'description')
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
              'description')
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
