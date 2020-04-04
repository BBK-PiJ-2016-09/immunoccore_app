from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from .models import Gene
from .serializers import GeneSerializer


class GeneViewSet(GenericViewSet,  # generic view functionality
                  CreateModelMixin,  # handles POSTs
                  RetrieveModelMixin,  # handles GETs for 1 Company
                  UpdateModelMixin,  # handles PUTs and PATCHes
                  ListModelMixin):  # handles GETs for many Companies
    """
    Class to add full put, post get functionality
    """
    serializer_class = GeneSerializer
    queryset = Gene.objects.all()
