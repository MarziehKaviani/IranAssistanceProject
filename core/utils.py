from rest_framework.response import Response
from typing import Optional, Any


class BaseResponse(Response):
    """
    Custom response class for standardized API responses.

    Args:
        http_status_code (int): HTTP status code for the response.
        business_status_code (int): Application-specific status code.
        is_exception (bool): Flag indicating if the response is due to an exception. Defaults to False.
        message (Optional[str]): Optional message to include in the response.
        data (Optional[Any]): Optional data to include in the response.
    """    

    def __init__(
        self, 
        http_status_code: int, 
        business_status_code: int, 
        is_exception: bool = False, 
        message: Optional[str] = None, 
        data: Optional[Any] = None
    ) -> None:
        
        super().__init__(
            data={
                "data": data,
                "message": message,
                'business_status_code': business_status_code
            },
            status=http_status_code,
            exception=is_exception
        )
