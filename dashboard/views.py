import json
from django.views.generic import TemplateView
from .models import Information_Book_Detail, Information_User_Detail, User_Rating_Information


class QueryResultsView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['data'] = {}

        return context

    def get_top_10_author(self):
        [
            {
                'id': obj.id,
                'value': obj.value,
                'date': obj.date.isoformat()
            }
            for obj in Information_Book_Detail.objects.all()
        ]