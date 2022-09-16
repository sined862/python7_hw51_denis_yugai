from django.urls import path, include
from cat.views.stats import stats_view
from cat.views.base import index_view



urlpatterns = [
    path('', index_view),
    path('cat_stats/', stats_view) 
]