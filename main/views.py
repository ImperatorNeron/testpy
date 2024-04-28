from django.views.generic import ListView, TemplateView

from .models import TestModel


class TestView(TemplateView):
    template_name = "main/index.html"
