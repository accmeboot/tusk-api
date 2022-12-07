from rest_framework.viewsets import ModelViewSet
from labels.models import Label

from labels.serializers import LabelSerializer


class LabelsViewSet(ModelViewSet):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
