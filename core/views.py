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
    serializer_class = CompleteDataSerializer

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
        # try:
        mapping_key = {
            "hfksjfesjfl": "insured_person",
            "provider": "insurance_provider",
            "holder": "policy_holder",
            "policy": "insurance_policy",
            "plan": "insurance_plan"
            }
        insurance_service = InsuranseService(serializer.validated_data, mapping_key)
        insurance_data = insurance_service.process_insurance_data()
        return BaseResponse(
        data={"Insurance policy unique identifier":insurance_data[variables.INSURANCE_POLICY][variables.UNIQUE_IDENTIFIER]},
        http_status_code=status.HTTP_200_OK, 
        business_status_code=BusinessStatusCodes.SUCCESS,
        )        
        # except Exception as e: #TODO
            # return BaseResponse(
            #     message=f"{variables.SOMETHING_WENT_WRONG}{e}", 
            #     http_status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            #     is_exception=True,
            #     business_status_code=BusinessStatusCodes.UNEXPECTED_ERROR
            #     )