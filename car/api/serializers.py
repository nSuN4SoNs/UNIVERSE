from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from car.models import Company

class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = ['name']
