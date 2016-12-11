
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
def hic_list(request, format=None):
    """
    List all snippets or create a new shelter tally.
    """

    if request.method == 'GET':
        shelters = HistoryHic.objects.all()
        print('INFO: shelter_list')
        serializer = HicSerializer(shelters, many=True)
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HicWriteSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def pit_list(request, format=None):
    """
    List all snippets or create a new population tally.
    """

    if request.method == 'GET':
        populations = HistoryPitSummary.objects.all()
        print('INFO: population_list')
        serializer = PitSerializer(populations, many=True)
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PitWriteSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
