from rest_framework.serializers import ModelSerializer

from apps.main.models import Feedback, Info, RulesOfUsing


class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ("id", "working_time", "email", "phone", "metro", "map")


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("id", "full_name", "phone", "text")


class RulesOfUsingSerializer(ModelSerializer):
    class Meta:
        model = RulesOfUsing
        fields = ("id", "title", "content")
