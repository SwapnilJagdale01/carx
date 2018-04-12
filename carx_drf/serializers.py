from rest_framework import serializers
from carx_drf.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'mobile', 'email', 'password', 'profilepic', 'socialId', 'otp', 'status')



