import django_filters
from django_filters import DateFilter
from .models import Tryout

class TryoutFilter(django_filters.FilterSet):
    class Meta:
        model = Tryout
        fields = '__all__'
        exclude = ["updated_at", "status"]