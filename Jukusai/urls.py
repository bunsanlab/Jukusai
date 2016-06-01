from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from program.views import programViewSet,photoViewSet,placeViewSet,voteViewSet

router = routers.DefaultRouter()
router.register(r'program',programViewSet)
router.register(r'photo',photoViewSet)
router.register(r'place',placeViewSet)
router.register(r'vote',voteViewSet)



urlpatterns = [
    # Examples:
    # url(r'^$', 'Jukusai.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace='api')),
]
