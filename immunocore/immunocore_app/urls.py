from django.urls import path, re_path, include
from .views import (
    GeneDetailView,
    GeneListView,
    index,
)
from .views.routers import router

urlpatterns = [
    path('', index, name='index'),
    path('genes/', GeneListView.as_view(), name='genes'),
    path('gene/<int:pk>', GeneDetailView.as_view(), name='gene-detail'),
    re_path('^', include(router.urls)),
]
