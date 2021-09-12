from rest_framework import serializers

from mainapp import models as mainModels
from daytask import models as daytaskModels


class PuplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = mainModels.Puples
        fields = ('id', 'name', 'surname', 'rate', 'status', 'email', 'phone', 'image')


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = mainModels.Events
        fields = ('id', 'name', 'date', 'organization', 'event_rate', 'verification_file', 'events', 'check')


class EventsActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = mainModels.EventActive
        fields = ('id', 'name', 'date', 'discription', 'link')


class DayTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = daytaskModels.Tasks
        fields = ('id', 'date', 'name', 'discription_task', 'status_task', 'result', 'count_answer', 'score', 'tries', 'tries_list', 'id_puple_correct_answers')
