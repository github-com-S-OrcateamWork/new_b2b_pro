from django_filters import rest_framework as filters
from .models import Product, Category
import datetime


class ProductFilter(filters.FilterSet):
    search = filters.CharFilter(field_name='translations__name', lookup_expr='icontains')
    popular = filters.BooleanFilter(field_name='views', method='filter_popular')

    class Meta:
        model = Product
        fields = ['category', 'search']

    def filter_category(self, queryset, name, value):
        return queryset.filter(categories__slug__icontains=value)
    
    def filter_popular(self, queryset, name, value):
        if value:
            return queryset.all().order_by('-created_at__year', '-views')
        return queryset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['category'].label = 'Category'
        self.filters['search'].label = 'Search'
        self.filters['popular'].label = 'Popular'