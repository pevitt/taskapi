from rest_framework import serializers


class TaskInputSerializer(serializers.Serializer):
    person_id = serializers.UUIDField()
    title = serializers.CharField(
        max_length=100
    )
    description = serializers.CharField()


class TaskOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    person_id = serializers.UUIDField()
    title = serializers.CharField(
        max_length=100
    )
    description = serializers.CharField()
    status = serializers.CharField(
        max_length=100
    )
    order = serializers.IntegerField()

class TaskOutputFullSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    person_name = serializers.CharField()
    person_email = serializers.CharField()
    title = serializers.CharField(
        max_length=100
    )
    description = serializers.CharField()
    status_name = serializers.CharField(
        max_length=100
    )
    order = serializers.IntegerField()
