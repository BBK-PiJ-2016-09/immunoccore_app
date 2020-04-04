from django.db import models
from django.urls import reverse
from immunocore_app.helpers.exceptions import GeneValidationException


NUCLEOTIDES = (
    'A',
    'T',
    'C',
    'G',
    'a',
    't',
    'c',
    'g',
)

class Gene(models.Model):
    """
    Modelling a gene as an abstract entity
    """
    name = models.CharField(max_length=200, help_text='Name of the gene')
    comments = models.CharField(max_length=1000, help_text='Comments on the gene')
    sequence = models.CharField(max_length=5000, help_text='DNA sequence, in {}'.format(NUCLEOTIDES))

    def save(self, *args, **kwargs):
        """
        Overwrite the save method to check the sequence only contains Dna
        :param args: any args
        :param kwargs: any kwargs
        :return: None, raises Exception
        """
        for n in self.sequence:
            if n not in NUCLEOTIDES:
                # TODO: Return this in the http response
                raise GeneValidationException('Nucleotide not accepted {} not in {}'.format(n, NUCLEOTIDES))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Gets the absolute url for the entity
        :return: A path within the app to the entity
        """
        return reverse('gene-detail', args=[str(self.id)])

    def get_google_url(self):
        """
        Gets a google search url for the gene
        :return: A link to google
        """
        return ('https://www.google.com/search?q={}'.format(self.name))
