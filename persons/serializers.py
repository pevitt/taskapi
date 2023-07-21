from rest_framework import serializers
from persons.models import Person

class PersonInputSerializer(
    serializers.Serializer
):
    first_name = serializers.CharField(
        max_length=100,
        required=True
    )
    last_name = serializers.CharField(
        max_length=100,
        required=True
    )
    email = serializers.EmailField(
        max_length=100,
        required=True
    )
    address = serializers.CharField(
        max_length=200,
        required=True
    )
    city = serializers.CharField(
        max_length=100,
        required=True
    )
    country = serializers.CharField(
        max_length=100,
        required=True
    )

class PersonOutputSerializer(
    serializers.Serializer
):
    id = serializers.UUIDField()
    first_name = serializers.CharField(
        max_length=100,
        required=True
    )
    last_name = serializers.CharField(
        max_length=100,
        required=True
    )
    email = serializers.EmailField(
        max_length=100,
        required=True
    )
    address = serializers.CharField(
        max_length=200,
        required=True
    )
    city = serializers.CharField(
        max_length=100,
        required=True
    )
    country = serializers.CharField(
        max_length=100,
        required=True
    )