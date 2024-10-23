from rest_framework import status, views, response
from rest_framework.decorators import action

from .serializer import CompleteDataSerializer
from .permissins import IsProviderPermission
from .serializer import CompleteDataSerializer
from .utils import BaseResponse
from core import variables
from core.variables import BusinessStatusCodes
from core.services.insurance_service import InsuranseService


class CreateInsuredPersonView(views.APIView):
    
    permission_classes = [IsProviderPermission]
    http_method_names = ['post']
    
    def post(self, request, *args, **kwargs):
        serializer = CompleteDataSerializer(data=request.data)
        if not serializer.is_valid():
            return BaseResponse(
                message=variables.INVALID_INPUT_DATA,
                data={variables.DETAILS: serializer.errors},
                is_exception=True,
                http_status_code=status.HTTP_400_BAD_REQUEST,
                business_status_code=BusinessStatusCodes.INVALID_INPUT_DATA,
            )
        try:
            insurance_service = InsuranseService()
            insurance_data = insurance_service.process_insurance_data()
            return BaseResponse(
            data=insurance_data,
            http_status_code=status.HTTP_200_OK, 
            business_status_code=BusinessStatusCodes.SUCCESS,
            )        
        except Exception as e:
            return BaseResponse(
                message=variables.SOMETHING_WENT_WRONG, 
                http_status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                is_exception=True,
                business_status_code=BusinessStatusCodes.UNEXPECTED_ERROR
                )