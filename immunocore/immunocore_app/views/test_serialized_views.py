from django.test import TestCase
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from .serialized_views import GeneViewSet


class GeneViewSetTestCase(TestCase):
    def setUp(self):
        self.gene_view_set = GeneViewSet()

    def test_inheritance(self):
        for class_mixin in [GenericViewSet,  CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin]:
            self.assertIsInstance(self.gene_view_set, class_mixin)
