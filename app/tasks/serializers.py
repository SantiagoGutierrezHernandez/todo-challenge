from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import Task, TaskState


class TaskStateSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TaskState
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ["id", "title", "description", "state"]

    def validate(self, attrs):

        user = attrs.get("user") or getattr(self.instance, "user", None)
        state = attrs.get("state") or getattr(self.instance, "state", None)

        if state and state.user != user:
            raise serializers.ValidationError(
                {"state": _("The selected state does not belong to this user.")}
            )
        return attrs