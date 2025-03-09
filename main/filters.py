from django_filters import FilterSet, DateFilter
from .models import Tryout

class TryoutFilter(FilterSet):
    date = DateFilter(field_name="created_at", lookup_expr='gte', label='Created at (from)')
    class Meta:
        model = Tryout
        fields = '__all__'
        exclude = ["created_at","updated_at", "status"]