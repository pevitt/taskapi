from enum import Enum

from rest_framework import status
from rest_framework.exceptions import APIException

class ErrorCode(Enum):
    E00 = dict(
        status=status.HTTP_400_BAD_REQUEST, 
        message='An unexpected error occurred, try again'
    )
    B01 = dict(
        status=status.HTTP_400_BAD_REQUEST,
        message='The email already exists'
    )
    B02 = dict(
        status=status.HTTP_404_NOT_FOUND,
        message='The email does not exist'
    )

    @classmethod
    def get_by_message(cls, message: str):
        try:
            return next(
                error for error in cls
                if error.value['message'] == message
            )
        except (Exception,):
            return cls.E00

    @classmethod
    def get_by_code(cls, code: str):
        try:
            return next(
                error for error in cls
                if error.name == code
            )
        except (Exception,):
            return cls.E00
        
class TaskManagerException(APIException):
    
    def __init__(
        self,
        error_code: ErrorCode = None,
        message: str = None
    ):
        error = error_code
        if message:
            error = ErrorCode.get_by_message(message)
        data = error.value
        self.status_code = data['status']
        super().__init__(detail=data['message'], code=data['status'])


