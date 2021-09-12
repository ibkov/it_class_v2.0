import datetime

from django.contrib.auth.models import User
from djoser.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from mainapp.addons_python.views_addons_functions import recount_all_peoples_rating
from mainapp import models as mainModels
from daytask import models as daytaskModels
from . import serializers

from rest_framework.decorators import action
from django.db.models import Q


class PuplesRateViewset(viewsets.ModelViewSet):
    queryset = mainModels.Puples.objects.order_by("-rate")
    serializer_class = serializers.PuplesSerializer

    def get_queryset(self):
        recount_all_peoples_rating()
        return mainModels.Puples.objects.order_by("-rate")

    @action(detail=True)
    def filter(self, request, pk=None):
        recount_all_peoples_rating()
        u = mainModels.Puples.objects.get(id=pk)
        if u.status == 'ST10' or u.status == 'ST11':
            recent_users = mainModels.Puples.objects.filter(status=u.status).order_by("-rate")
        else:
            recent_users = mainModels.Puples.objects.order_by("-rate")
        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


class PuplesDetailViewset(viewsets.ModelViewSet):
    queryset = mainModels.Puples.objects.all()
    serializer_class = serializers.PuplesSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk:
            return mainModels.Puples.objects.get(user=User.objects.get(id=pk))

        return super(PuplesDetailViewset, self).get_object()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super(UserViewSet, self).get_object()


class EventsViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        # pk = self.kwargs.get('pk')

        if 'pk' in self.kwargs:
            return mainModels.Events.objects.filter(events=self.kwargs['pk']).order_by("-date")
        else:
            return mainModels.Events.objects.order_by("-date")

    serializer_class = serializers.EventsSerializer

    def retrieve(self, request, *args, **kwargs):  # Change is here <<
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)


class DayTaskViewset(viewsets.ModelViewSet):
    queryset = daytaskModels.Tasks.objects.filter(date=datetime.date.today())
    serializer_class = serializers.DayTaskSerializer


class EventsActiveViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        a = [i.id for i in mainModels.EventActive.objects.all().order_by('date') if i.date >= datetime.datetime.now().date()]
        print(a)
        return mainModels.EventActive.objects.filter(id__in=a).order_by('date')
    serializer_class = serializers.EventsActiveSerializer
