from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from car.models import Company
from car.api.serializers import CompanySerializer

class CompanyViewSet(ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
