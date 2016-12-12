
from rest_framework import serializers
from tallyapp.models import *

class PitSerializer(serializers.ModelSerializer):
    """
    Serializer for GET/POST operations on Point-In-Time (PIT) tally.
    """

    class Meta:
        model = HistoryPitSummaryAPI
        fields = ('id', 'Table', 'Population', 'SubPopulation', 'Date', 'Value')

class PitWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for PUT/DELETE operations on Point-In-Time (PIT) tally.
    """

    populations = serializers.PrimaryKeyRelatedField(queryset=HistoryPitSummaryAPI.objects.all(), allow_null=True)

    class Meta:
        model = HistoryPitSummaryAPI
        fields = ('id', 'Table', 'Population', 'SubPopulation', 'Date', 'Value')

class PitSubSerializer(serializers.ModelSerializer):
    """
    Serializer for GET/POST operations on PIT sub-populations.
    """

    class Meta:
        model = HistoryPitSubpopulationsAPI
        fields = ('id', 'Table', 'Population', 'Shelter', 'Date', 'Value')

class PitSubWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for PUT/DELETE operations on PIT sub-populations.
    """

    populations = serializers.PrimaryKeyRelatedField(queryset=HistoryPitSubpopulationsAPI.objects.all(), allow_null=True)

    class Meta:
        model = HistoryPitSubpopulationsAPI
        fields = ('id', 'Table', 'Population', 'Shelter', 'Date', 'Value')

class HicSerializer(serializers.ModelSerializer):
    """
    Serializer for GET/POST operations on shelters.
    """

    class Meta:
        model = HistoryHicAPI
        fields = ('id', 'Table', 'Shelter', 'UnitBed', 'Date', 'Value')

class HicWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for PUT/DELETE operations on shelters.
    """

    shelters = serializers.PrimaryKeyRelatedField(queryset=HistoryHicAPI.objects.all(), allow_null=True)

    class Meta:
        model = HistoryHicAPI
        fields = ('id', 'Table', 'Shelter', 'UnitBed', 'Date', 'Value')
