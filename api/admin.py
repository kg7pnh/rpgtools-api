# -*- coding: utf-8 -*-
"""
Registers modesl for the admin section
"""
from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget
from api.models.book import Book
from api.models.book_format import BookFormat
from api.models.schema import Schema
from api.models.game import Game
from api.models.publisher import Publisher

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
              'edition_id',
              'name',
              'short_name',
              'abbreviation',
              'edition',
              'publisher',
              'game',
              'book_format',
              'created',
              'modified',
              'description')
    readonly_fields = ('_id',
                       'id',
                       'edition_id',
                       'created',
                       'modified')
    list_display = ('name',
                    'edition',
                    'created',
                    'modified',
                    'id',
                    'edition_id',
                    '_id')

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
              'version',
              'publisher',
              'created',
              'modified',
              'description')
    readonly_fields = ('_id',
                       'id',
                       'created',
                       'modified')
    list_display = ('name',
                    'version',
                    'created',
                    'modified',
                    'id',
                    '_id')

admin.site.register(Game, GameAdmin)

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
              'schema_type',
              'specification',
              'description',
              'read_me')
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
