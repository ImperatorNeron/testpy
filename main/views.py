from django.views.generic import ListView, TemplateView

from main.models import TestModel


class TestView(TemplateView):
    template_name = "main/index.html"
