from rest_framework import serializers
from django.db import models
from .models import Customer, Profession


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'address', 'professions', 'data_sheet']

class  ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'description')