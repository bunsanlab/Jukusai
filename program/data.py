from program.models import program, place
from datetime import datetime, timedelta

placeData =[
    {
        "placeName":"2F",
        "room":"214"
    },
    {
        "placeName":"4F",
        "room":"424"
    },
    {
        "placeName":"5F",
        "room":"534"
    },
    {
        "placeName":"3F",
        "room":"314"
    }
]

programData =[
    {
        "groupName":"tako",
        "contentName":"ika",
        "contentData":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "category":1,
        "place":1,
        "firstFlag":False,
        "secondFlag":True,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"kurage",
        "contentName":"takoyaki",
        "contentData":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        "category":2,
        "place":1,
        "firstFlag":False,
        "secondFlag":True,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    }
]

def createdata():
    for i in placeData:
        pl = place.objects.create(
            placeName  =i['placeName'],
            room       =i['room']
        )
    for i in programData:
        pro = program.objects.create(
            groupName  =i['groupName'],
            contentName=i['contentName'],
            contentData=i['contentData'],
            category   =i['category'],
            place      = place.objects.get(pk=i['place']),
            firstFlag  =i['firstFlag'],
            secondFlag =i['secondFlag'],
            thirdFlag  =i['thirdFlag'],
            allFlag    =i['allFlag'],
            start_at   =i['start_at'],
            end_at     =i['end_at']
        )

