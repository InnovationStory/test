import django_filters
from classroom.models import Process


class ProcessFilter (django_filters.FilterSet):
    u__contains = django_filters.rest_framework.CharFilter(field_name='process_name', lookup_expr='icontains')


    class Meta:
        model =Process
        fields = ['u__contains',]

