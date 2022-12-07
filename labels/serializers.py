from rest_framework import serializers

from labels.models import Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"


class LabelTaskPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ("id",)
