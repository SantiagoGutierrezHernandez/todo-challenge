import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    created_on = django_filters.DateFromToRangeFilter(field_name="created_on")
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    description = django_filters.CharFilter(field_name="description", lookup_expr="icontains")
    state = django_filters.BaseInFilter(field_name="state")

    class Meta:
        model = Task
        fields = ["created_on", "title", "description", "state"]