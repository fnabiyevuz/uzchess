from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.main.models import Feedback, Info, RulesOfUsing
from apps.main.serializers import (FeedbackSerializer, InfoSerializer,
                                   RulesOfUsingSerializer)


@api_view(["GET"])
def get_info(request):
    try:
        info = Info.objects.last()
        serializer = InfoSerializer(info)
        return Response(serializer.data)
    except Exception as e:
        return Response({"Error": f"{e}"})


class FeedbackCreateApiView(CreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


@api_view(["GET"])
def get_rulesofuseing(request):
    try:
        info = RulesOfUsing.objects.last()
        serializer = RulesOfUsingSerializer(info)
        return Response(serializer.data)
    except Exception as e:
        return Response({"Error": f"{e}"})
