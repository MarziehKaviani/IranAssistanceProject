from django.urls import path
from .views import CreateInsuredPersonView


urlpatterns = [
    path('api/insurance-policy/', CreateInsuredPersonView.as_view(), name='insurance-policy'),
]