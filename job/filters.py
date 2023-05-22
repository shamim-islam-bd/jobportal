
from django_filters import rest_framework as filters
from .models import Job

class JobsFilter(filters.FilterSet):
    
    # it'll check min_salary greater than or equal to 0 and max_salary less than 1000000 or equal to salary
    min_salary = filters.NumberFilter(field_name='salary' or 0, lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name='salary' or 1000000, lookup_expr='lte')
    
    # it'll check title, address contains keyword or not 
    keyword = filters.CharFilter(field_name='title', lookup_expr='icontains')
    location = filters.CharFilter(field_name='address', lookup_expr='icontains')
    
    
    class Meta:
        model = Job
        fields = ('jobType', 'education', 'industry', 'experience', 'min_salary', 'max_salary', 'keyword', 'location')
