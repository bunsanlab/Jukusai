from rest_framework import serializers
from imageline.models import photo, token
from program.programSerializer import programSimpleSerializer


class tokenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = token
        fields = ('pk', 'key', 'created_at',)


class photoSerializer(serializers.HyperlinkedModelSerializer):
    program = programSimpleSerializer()

    class Meta:
        model = photo
        fields = ('pk', 'program', 'path', 'publicFlag', 'created_at',)
