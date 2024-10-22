from rest_framework import status, views, response
from rest_framework.decorators import action

from .serializer import CompleteDataSerializer
from .builders import DataBuilder
from .permissins import IsProviderPermission
from .serializer import CompleteDataSerializer
from .utils import BaseResponse
from core import variables
from core.variables import BusinessStatusCodes
from Insurance.models import InsuredPerson


class CreateInsuredPersonView(views.APIView):
    permission_classes = [IsProviderPermission]
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        # Send data to serializer
        serializer = CompleteDataSerializer(data=request.data)
        if not serializer.is_valid():
            return BaseResponse(
                message=variables.INVALID_INPUT_DATA,
                data={variables.DETAILS: serializer.errors},
                is_exception=True,
                http_status_code=status.HTTP_400_BAD_REQUEST,
                business_status_code=BusinessStatusCodes.INVALID_INPUT_DATA,
            )
        # Build the data
        try:
            data_builder = DataBuilder(serializer.validated_data)
            created_data = data_builder.build()

            # return BaseResponse(
            # data=created_data,
            # http_status_code=status.HTTP_200_OK, 
            # business_status_code=BusinessStatusCodes.SUCCESS,
            # )
        except Exception as e:
            return BaseResponse(
                message=variables.SOMETHING_WENT_WRONG, 
                http_status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                is_exception=True,
                business_status_code=BusinessStatusCodes.UNEXPECTED_ERROR
                )
    