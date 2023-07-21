# Django
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from persons.serializers import PersonInputSerializer, PersonOutputSerializer
from persons import services as person_services
from utils.exceptions import TaskManagerException, ErrorCode

# Create your views here.
class PersonView(
    APIView
):
    def post(self, request):
        
        in_serializer = PersonInputSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)

        data = person_services.create_person(
            **in_serializer.validated_data
        )

        out_serializer = PersonOutputSerializer(data=data.__dict__)
        try:
            out_serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            raise TaskManagerException(ErrorCode.E00)

        return Response(out_serializer.data, status=201)
    
    
    class InputGetSerializer(serializers.Serializer):
            email = serializers.EmailField()

    def get(self, request):
        
        in_serializer = self.InputGetSerializer(data=request.query_params.dict())
        in_serializer.is_valid(raise_exception=True)
    
        data = person_services.get_person(
            **in_serializer.validated_data
        )
        out_serializer = PersonOutputSerializer(data=data.__dict__)

        try:
            out_serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            raise TaskManagerException(ErrorCode.E00)

        return Response(out_serializer.data, status=200)


