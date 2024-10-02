# movies/filters.py

import django_filters
from .models import Moviescontent

class MovieFilter(django_filters.FilterSet):
    year_of_release = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    language = django_filters.CharFilter(field_name='original_language')

    class Meta:
        model = Moviescontent
        fields = ['year_of_release', 'language']
