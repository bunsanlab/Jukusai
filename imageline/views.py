from rest_framework import status, viewsets
from rest_framework.decorators import list_route, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

from program.models import program
from imageline.models import photo, token
from imageline.imagelineSerializer import photoSerializer, tokenSerializer



PHOTOPATH = '~/Develop/django/Jukusai/static/img/'


def Jukusai_authentication(Token):
    try:
        post = token.objects.get(key=Token)
        if(post.banFlag):
            return 0
        return post
    except:
        return 0


class photoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = photo.objects.all()
    serializer_class = photoSerializer


    @list_route(methods=['GET'])
    def token(self, request):
        Token = token.objects.create()
        data = tokenSerializer(Token)
        return Response(data.data)

    @list_route(methods=['POST'])
    def post(self, request, format=None):
        try:
            json_str = request.body.decode('utf-8')
            jsonData = json.loads(json_str)
            pk = Jukusai_authentication(jsonData['token'])
            pk = jsonData['program']
            pro = program.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if(post.pk==0):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        print(request.FILES)
        print(request.data)
        try:
            f = open('')
            f.write(request.FILES['file'])
            f.close()
            data = photo.objects.create(program=pro,path="",token=token)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_200_OK)

    @list_route(methods=['GET'])
    def imageline(self, request):
        data = photo.objects.filter(publicFlag=False)
        serializers = self.serializer_class(data)
        return Response(serializers.data)





