from django.urls import path
from .views import load_csv, index

urlpatterns = [
    path('', load_csv, name='load-csv'),
]
