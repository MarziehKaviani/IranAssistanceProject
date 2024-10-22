from rest_framework.response import Response


class BaseResponse(Response):
    def __init__(self,  http_status_code, business_status_code, is_exception=False, message=None, data=None) -> None:
        super().__init__(
            data={
                "data": data,
                "message": message,
                'business_status_code': business_status_code
            },
            status=http_status_code,
            exception=is_exception
        )
