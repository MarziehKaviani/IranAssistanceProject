from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


swagger_description = """
### IranAssistanceProject APIs
  
    `Summery`: This API receives bulk insurance data from various insurance providers (e.g., Pasargad, Hekmat, Mellat, Saman, etc.).
    The providers submit a unified JSON containing personal, insurance, policyholder, and plan details. The API validates and processes the data,
    ensuring compliance with our business rules. Each section, such as personal details, insurance provider info, policyholder details,
    insurance policy, and plan specifics, follows a strict format and sequence. Validation includes email, mobile number, national ID,
    and required fields. The API supports custom field names for different providers while adhering to business logic. Proper error handling
    and validation messages are implemented.


`_________________________________________________________________`
    
"""

schema_view = get_schema_view(
    openapi.Info(
        title="APIs",
        default_version="v1",
        description=swagger_description,
        contact=openapi.Contact(email=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('core.urls')),
]
