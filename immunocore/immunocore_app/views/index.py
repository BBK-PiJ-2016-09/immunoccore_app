from django.shortcuts import render
from ..models import (
    Gene,
)


def index(request):
    # Generate counts of the main objects
    gene_counts = Gene.objects.all().count()

    context = {
        'gene_counts': gene_counts,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
