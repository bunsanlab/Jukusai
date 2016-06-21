from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from program.views import programViewSet,placeViewSet,voteViewSet
from imageline.views import photoViewSet

router = routers.DefaultRouter()
router.register(r'program',programViewSet)
router.register(r'place',placeViewSet)
router.register(r'vote',voteViewSet)
router.register(r'image',photoViewSet)



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace='api')),
]

