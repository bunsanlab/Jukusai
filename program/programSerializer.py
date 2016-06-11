from rest_framework import serializers
from .models import program,place,photo,vote

class placeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = place
        fields = ('pk', 'placeName', 'room',)
        lookup_field='placeName'

class placeSimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = place
        fields = ('placeName',)

class programSerializer(serializers.HyperlinkedModelSerializer):
    place = placeSimpleSerializer()
    class Meta:
        model = program
        fields = ('pk',
                  'groupName',
                  'contentName',
                  'contentData',
                  'category',
                  'place',
                  'firstFlag',
                  'secondFlag',
                  'thirdFlag',
                  'allFlag',
                  'start_at',   
                  'end_at',     
                  'created_at',
                  'updated_at') 

class programSimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = program
        fields = ('pk', 'groupName', 'contentName', 'category',)

class photoSerializer(serializers.HyperlinkedModelSerializer):
    program = programSimpleSerializer()
    class Meta:
        model = photo
        fields = ('pk', 'program', 'path', 'publicFlag', 'created_at',)


class voteSerializer(serializers.HyperlinkedModelSerializer):
    program = programSimpleSerializer()
    class Meta:
        model = vote
        fields = ('pk', 'program', 'num',)

