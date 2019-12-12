# -*- coding: utf-8 -*-
"""
history serializer
"""
from django.db.models import ManyToManyRel
from django.db.models import ManyToOneRel
from rest_framework import serializers

class HistorySerializer(serializers.Serializer): # pylint: disable=abstract-method
    """
    Publisher history serializer
    """
    changes = serializers.SerializerMethodField()

    def get_changes(self, obj): # pylint: disable=no-self-use
        """
        get_changes
        """
        changes = []
        for record in obj.history.all():
            _change = {
                "type": record.get_history_type_display(),
                "changes": []
            }
            if _change["type"] == "Created":
                for field in record.history_object._meta.get_fields(): # pylint: disable=protected-access
                    if not isinstance(field, ManyToOneRel) \
                        and not isinstance(field, ManyToManyRel) \
                        and not field.primary_key \
                        and field.editable \
                        and not field.blank:
                        value = getattr(record.history_object, field.name)
                        _change["changes"].append({
                            "old": None,
                            "new": value,
                            "field": field.name
                        })
                    # elif isinstance(field, ForeignKey):
                    #     related_objs = getattr(
                    #         record.history_object, field.name)
                    #     _change["changes"].append({
                    #         "old": None,
                    #         "len": len(related_objs),
                    #         "type": field.__class__.__name__,
                    #         "field": field.name
                    #     })

            else:
                delta = record.diff_against(record.prev_record)
                _change["changes"].extend(
                    [change.__dict__ for change in delta.changes])
            changes.append(_change)
        return changes
