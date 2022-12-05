from rest_framework import serializers, exceptions

from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "name",
            "status",
        )

    def create(self, validated_data):
        request = self.context.get("request")

        if request and hasattr(request, "user"):
            user = request.user
            project = Project.objects.create(
                name=validated_data["name"],
                status=validated_data["status"],
                created_by=user,
            )
            project.save()

            return project

        raise exceptions.APIException("Something whent wrong")
