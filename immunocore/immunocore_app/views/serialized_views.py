from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from ..models import Gene
from ..serializers import GeneSerializer


class GeneViewSet(GenericViewSet,  CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    """
    Class to add full put, post get functionality
    """
    serializer_class = GeneSerializer
    queryset = Gene.objects.all()
