from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-tryout/', tryout_create, name='create_tryout'),
    path('edit_tryout/<int:id>/', tryout_edit, name='tryout_edit'),
    path('delete_tryout/<int:id>/', tryout_delete, name='tryout_delete'),
    path('detail_tryout/<int:id>/', tryout_detail, name='tryout_detail'),
]
