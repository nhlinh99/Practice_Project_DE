from django.urls import path
from django.views.generic.base import TemplateView

# http://127.0.0.1/dashboard/
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
]
