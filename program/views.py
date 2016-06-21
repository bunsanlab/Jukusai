from rest_framework import status, viewsets
from rest_framework.decorators import list_route, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from Jukusai.jsonResponse import JSONResponse

from program.programSerializer import programSerializer, placeSerializer, voteSerializer
from program.models import program, place,  vote

import json


class programViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = program.objects.all()
    serializer_class = programSerializer
    http_method_names = ['get']

    @list_route(renderer_classes=[JSONRenderer], methods=['get'])
    def get_pagenate(self, request):
        data = program.objects.all()
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    @list_route(renderer_classes=[JSONRenderer], methods=['get'])
    def stage(self, request):
        data = program.objects.filter(category=1).order_by('start_at')
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    @list_route(renderer_classes=[JSONRenderer], methods=['get'])
    def stall(self, request):
        data = program.objects.filter(category=2)
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    @list_route(renderer_classes=[JSONRenderer], methods=['get'])
    def room(self, request):
        data = program.objects.filter(category=3)
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    @list_route(renderer_classes=[JSONRenderer], methods=['get'])
    def lab(self, request):
        data = program.objects.filter(category=4)
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    @list_route(renderer_classes=[JSONRenderer], methods=['get'])
    def ranking(self, request):
        data = vote.objects.all().order_by('num')
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = voteSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = voteSerializer(data, many=True)
        return Response(serializer.data)


class placeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = place.objects.all()
    serializer_class = placeSerializer


class voteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = vote.objects.all()
    serializer_class = voteSerializer

    @list_route(methods=['post'])
    def add(self, request, pk=None):
        try:
            json_str = request.body.decode('utf-8')
            pk = json.loads(json_str)
            pk = int(pk['pk'])
            proId = program.objects.get(pk=pk)
            data = vote.objects.get(program__pk=proId.pk)
            data.num = data.num + 1
            data.save()
            serializer = voteSerializer(data)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'])
    def delete(self, request, pk=None):
        try:
            json_str = request.body.decode('utf-8')
            pk = json.loads(json_str)
            pk = int(pk['pk'])
            proId = program.objects.get(pk=pk)
            data = vote.objects.get(program__pk=proId.pk)
            data.num = data.num - 1
            data.save()
            serializer = voteSerializer(data)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
