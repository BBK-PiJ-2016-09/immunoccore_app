from django.views.generic import ListView, DetailView
from ..models import Gene


class GeneDetailView(DetailView):
    model = Gene


class GeneListView(ListView):
    model = Gene
