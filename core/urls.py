from django.urls import path
from .views import CreateInsuredPersonView


urlpatterns = [
    path('insurance-policy/', CreateInsuredPersonView.as_view(), name='insurance-policy'),
]