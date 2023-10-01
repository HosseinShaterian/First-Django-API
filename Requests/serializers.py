from rest_framework import serializers
from .models import CustomerRequest


class CustomerRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = '__all__'
