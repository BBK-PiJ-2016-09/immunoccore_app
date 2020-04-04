from rest_framework.routers import DefaultRouter
from .serialized_views import GeneViewSet


router = DefaultRouter()
router.register('gene_router', GeneViewSet)
