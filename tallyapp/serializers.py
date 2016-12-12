
from rest_framework import serializers
from tallyapp.models import *

class HicSerializer(serializers.ModelSerializer):
    """
    Serializer for GET/POST operations on shelters.
    """

    class Meta:
        model = HistoryHicAPI
        fields = ('id', 'Shelter', 'BedType', 'Date')

class HicWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for PUT/DELETE operations on shelters.
    """

    shelters = serializers.PrimaryKeyRelatedField(queryset=HistoryHicAPI.objects.all(), allow_null=True)

    class Meta:
        model = HistoryHicAPI
        fields = ('id', 'Shelter', 'BedType', 'Date')

class PitSerializer(serializers.ModelSerializer):
    """
    Serializer for GET/POST operations on populations.
    """

    class Meta:
        model = HistoryPitSummaryAPI
        fields = ('id', 'Table', 'Population', 'SubPopulation', 'Date', 'Value')

class PitWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for PUT/DELETE operations on populations.
    """

    populations = serializers.PrimaryKeyRelatedField(queryset=HistoryPitSummaryAPI.objects.all(), allow_null=True)

    class Meta:
        model = HistoryPitSummaryAPI
        fields = ('id', 'Table', 'Population', 'SubPopulation', 'Date', 'Value')
