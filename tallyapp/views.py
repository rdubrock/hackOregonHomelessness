
# troys 10DEC original placeholder
#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("INFO (HttpResponse): tallyapp index page.")


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tallyapp.models import *
from tallyapp.serializers import *

# Uncomment to enable debug
#import pdb
#pdb.set_trace()


@api_view(['GET', 'POST'])
def pit_list(request, format=None):
    """
    List all snippets or create a new PIT tally.
    """

    if request.method == 'GET':
        populations = HistoryPitSummaryAPI.objects.all()
        serializer = PitSerializer(populations, many=True)
        print('INFO: GET PIT population_list')
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PitWriteSerializer(data=request.data)
        print('INFO: POST PIT population_list')
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pit_detail(request, pk, format=None):
    """
    Retrieve, update or delete a PIT tally instance.
    """
    try:
        tally = HistoryPitSummaryAPI.objects.get(pk=pk)
    except HistoryPitSummaryAPI.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedPit = PitSerializer(instance=tally)
        print('INFO: GET PIT pit_list')
        print(serializedPit)
        return Response(serializedPit.data)

    elif request.method == 'PUT':
        serializedPit = PitSerializer(tally, data=request.data) # takes data in and serializes to python
        if serializedPit.is_valid():
            serializedPit.save() # save the updated pit tally
            return Response(serializedPit.data)
        return Response(serializedPit.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tally.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def pitsub_list(request, format=None):
    """
    List all snippets or create a new subpopulation tally.
    """

    if request.method == 'GET':
        populations = HistoryPitSubpopulationsAPI.objects.all()
        serializer = PitSubSerializer(populations, many=True)
        print('INFO: GET PIT subpopulation_list')
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PitSubWriteSerializer(data=request.data)
        print('INFO: POST PIT subpopulation_list')
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def hic_list(request, format=None):
    """
    List all snippets or create a new shelter tally.
    """

    if request.method == 'GET':
        shelters = HistoryHicAPI.objects.all()
        serializer = HicSerializer(shelters, many=True)
        print('INFO: GET HIC shelter_list')
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HicWriteSerializer(data=request.data)
        print('INFO: POST HIC shelter_list')
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
