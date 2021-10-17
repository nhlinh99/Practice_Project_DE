from django.urls import path
from .views import dashboard_with_pivot

# http://127.0.0.1/dashboard/
urlpatterns = [
    path('', dashboard_with_pivot, name='dashboard'),
]
