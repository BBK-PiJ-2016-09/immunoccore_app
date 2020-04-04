from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Gene


class GeneSerializer(ModelSerializer):
    """
    Serializer for a gene (adapts the transport layer)
    """
    # Example of setting additional field in the serializer (e.g. implicit information we want to make explicit at
    # runtime)
    sequence_length = SerializerMethodField('get_sequence_length')

    def get_sequence_length(self, entity):
        return len(entity.sequence)

    class Meta:
        model = Gene
        fields = (
            'name', 'sequence', 'comments', 'sequence_length'
        )
