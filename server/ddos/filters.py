import django_filters


class SiteFilterSet(django_filters.FilterSet):
    status = django_filters.BooleanFilter(field_name='check_results__status')
