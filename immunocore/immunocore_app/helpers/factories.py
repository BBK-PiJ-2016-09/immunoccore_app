import random
from factory import DjangoModelFactory, Faker
from ..models import Gene


def gene_sequence_creator():
    """
    Helper function to create a proper gene_sequence, for testing only
    :return: A gene sequence of length 1--> 1000
    """
    ret_val = ''
    for i in range(1, random.randint(1, 1000)):
        ret_val += ['A', 'T', 'C', 'G', 'a', 't', 'c', 'g'][random.randint(0, 7)]
    return ret_val


class DefaultGeneFactory(DjangoModelFactory):
    """A factory for genes"""
    name = Faker('text')
    comments = Faker('text')
    sequence = Faker('text')

    class Meta:
        model = Gene


class GeneFactory(DefaultGeneFactory):
    """
    A modified factory for genes, exending the behaviour of sequence so that it only creates DNA
    """
    sequence = gene_sequence_creator()
