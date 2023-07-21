from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from utils.exceptions import TaskManagerException, ErrorCode
from tasks import services as task_service
from tasks.serializers import TaskInputSerializer, TaskOutputSerializer, TaskOutputFullSerializer

# Create your views here.
class TaskStatusView(
    APIView
):

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()


    def get(self, request, format=None):
        
        data = task_service.get_task_status_list()
        output_serializer = self.OutputSerializer(data=data, many=True)
        
        try:
            output_serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            raise TaskManagerException(ErrorCode.E00)

        return Response(output_serializer.data, status=200)
    
class TaskView(
    APIView
):
    def post(self, request):
        
        in_serializer = TaskInputSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)

        data = task_service.create_task(
            **in_serializer.validated_data
        )

        out_serializer = TaskOutputSerializer(data=data)
        try:
            out_serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            raise TaskManagerException(ErrorCode.E00)
        
        return Response(out_serializer.data, status=201)
    
    class InputGetSerializer(serializers.Serializer):
        person_id = serializers.UUIDField()
        status = serializers.CharField(
            required=False
        )

    def get(self, request):
        
        in_serializer = self.InputGetSerializer(data=request.query_params)
        in_serializer.is_valid(raise_exception=True)
        data = task_service.get_task_list(
            **in_serializer.validated_data
        )
        out_serializer = TaskOutputFullSerializer(data=data, many=True)
        try:
            out_serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            raise TaskManagerException(ErrorCode.E00)
        
        return Response(out_serializer.data, status=200)
    
    class InputPutSerializer(serializers.Serializer):
        task_id = serializers.UUIDField()
        status_id = serializers.IntegerField()

    def put(self, request):

        in_serializer = self.InputPutSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)

        data = task_service.update_task_status(
            **in_serializer.validated_data
        )
        out_serializer = TaskOutputFullSerializer(data=data)
        try:
            out_serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            raise TaskManagerException(ErrorCode.E00)
        
        return Response(out_serializer.data, status=200)

class TaskViewIndicator(
    APIView
):
    
    def get(self, request, person_id):
        
        data = task_service.get_task_person_indicator(
            person_id=person_id
        )

        return Response(data, status=200)
        
    
    

