from rest_framework import status, viewsets
from rest_framework.decorators import action

from core import variables
from .permissins import IsProviderPermission
from .serializer import CompleteDataSerializer


class GetInsuranceData(
    viewsets.GenericViewSet,
):
    """
    API endpoint that provides various actions related to Login.

    Attributes
    ----------
    * `queryset`: ``QuerySet``
        The set of all User objects.
    """
    # queryset = 
    permission_classes = [IsProviderPermission]
    serializer_class = CompleteDataSerializer

    # @action(detail=False, methods=[variables.POST])
   