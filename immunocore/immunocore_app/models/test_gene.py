from django.test import TestCase
from immunocore_app.helpers.factories import GeneFactory, DefaultGeneFactory


class GeneTestCase(TestCase):
    def setUp(self):
        self.gene = GeneFactory()

    def test_01_str(self):
        self.assertEqual(str(self.gene), self.gene.name)

    def test_02_sequence_is_made_of_nucleotides(self):
        self.assertTrue(all([n in ['A', 'T', 'C', 'G', 'a', 't', 'c', 'g'] for n in self.gene.sequence]))

    def test_03_assert_fail_with_non_standard_nucleotides(self):
        with self.assertRaises(Exception) as context:
            DefaultGeneFactory()

        self.assertTrue('Nucleotide not accepted' in str(context.exception))

    def test_04_url(self):
        self.assertEqual(self.gene.get_absolute_url(), '/immunocore_app/gene_router/1/')

    def test_05_url(self):
        self.assertEqual(self.gene.get_google_url(), 'https://www.google.com/search?q={}'.format(self.gene.name))
