from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'rate', views.PuplesRateViewset, basename="rate")
router.register(r'getuserdata', views.UserViewSet, basename="userdata")
router.register(r'getdetailuserdata', views.PuplesDetailViewset, basename="detailuserdata")
router.register(r'userevents', views.EventsViewset, basename="events")
router.register(r'daytask', views.DayTaskViewset, basename="daytask")
router.register(r'eventsactive', views.EventsActiveViewset, basename="eventsactive")
