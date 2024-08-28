from tkinter.font import names

import django_filters

from store.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',
                                     lookup_expr='icontains'),  ## filter name by any name that is entered without being completed
    maxPrice = django_filters.NumberFilter(field_name='price' or 0,
                                           lookup_expr='lte'),  ## brings price that is more than entered value
    minPrice = django_filters.NumberFilter(field_name='price' or 1000,
                                           lookup_expr='gte'),  ## brings price that is more than entered value

    class Meta:
        model = Product
        fields = '__all__'
