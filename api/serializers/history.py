# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

Returns:
    _type_: _description_
"""
from django.db.models import ManyToManyRel
from django.db.models import ManyToOneRel
from django.db.models.fields.related import ManyToManyField
from django.db.models.fields.related import ManyToManyRel
from rest_framework import serializers


class HistorySerializer(serializers.Serializer):  # pylint: disable=abstract-method
    # TODO: update docstring
    """_summary_

    Args:
        serializers (_type_): _description_

    Returns:
        _type_: _description_
    """
    changes = serializers.SerializerMethodField()

    def get_changes(self, obj):  # pylint: disable=no-self-use
        # TODO: update docstring
        """_summary_

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        changes = []
        for record in obj.history.all():
            change_count = 0
            _change = {
                "history_type": record.get_history_type_display(),
                "history_date_time": record.history_date,
                "history_id": record.history_id,
                "changes": []
            }
            if _change["history_type"] == "Created":
                for field in record.history_object._meta.get_fields():

                    if field.editable \
                            and not field.__class__.__name__ == 'ManyToManyField':
                        change_count += 1
                        value = str(getattr(record.history_object, field.name))
                        _change["changes"].append({
                            "field": field.name,
                            "new": value,
                            "old": None
                        })
                    elif field.__class__.__name__ == 'ManyToManyField':
                        result = []
                        try:
                            change_count += 1
                            items = getattr(
                                record.history_object, field.name).all()
                            for item in items:
                                result.append(str(item))
                        except:
                            pass
                        _change["changes"].append({
                            "field": field.name,
                            "new": result,
                            "old": None
                        })
                _change["change_count"] = change_count
            else:
                delta = record.diff_against(record.prev_record)
                for change in delta.changes:
                    change_count += 1
                    _change["changes"].append({
                        "field": change.__dict__["field"],
                        "old": change.__dict__["old"],
                        "new": change.__dict__["new"]
                    })
                _change["change_count"] = change_count
            changes.append(_change)
        return changes
