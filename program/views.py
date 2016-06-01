from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from Jukusai.jsonResponse import JSONResponse

from program.programSerializer import programSerializer,photoSerializer,placeSerializer,voteSerializer
from program.models   import program,place,photo,vote
from Jukusai.paginator import paginate
# Create your views here.

class programViewSet(viewsets.ModelViewSet):
    queryset = program.objects.all()
    serializer_class = programSerializer

    @list_route(renderer_classes=[JSONRenderer])
    def get_pagenate(self,request):
        data = program.objects.all()
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

class placeViewSet(viewsets.ModelViewSet):
    queryset = place.objects.all()
    serializer_class = placeSerializer

class photoViewSet(viewsets.ModelViewSet):
    queryset = photo.objects.all()
    serializer_class = photoSerializer

class voteViewSet(viewsets.ModelViewSet):
    queryset = vote.objects.all()
    serializer_class = voteSerializer

