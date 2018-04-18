from rest_framework import serializers
from carx_drf.models import Customer, Tyre


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'mobile', 'email', 'password', 'profilepic', 'socialId', 'otp', 'status')


class TyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tyre
        fields = ('id', 'make', 'model', 'image', 'category', 'pattern', 'description', 'warranty')
