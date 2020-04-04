from django.test import TestCase
from .index import index


class GeneTestCase(TestCase):
    def setUp(self):
        self.index = index({})

    def test_01_ret_val(self):
        self.assertEqual(str(self.index), '<HttpResponse status_code=200, "text/html; charset=utf-8">')
