from rest_framework import serializers
from carx_drf.models import Customer, Tyre
import pyotp


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'mobile', 'email', 'password', 'profilepic', 'socialId', 'otp', 'status')

    def create(self, validated_data):

            usertype = Customer.objects.create(**validated_data)
            totp = pyotp.TOTP('base32secret3232')
            totp.now()  # => '492039'

            usertype.otp = int(totp.now())
            usertype.save()
            return usertype


class TyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tyre
        fields = ('id',  'vehicle', 'category', 'pattern', 'description', 'warranty', 'product_type', 'normalsectionwidth', 'normalaspectratio', 'constructiontype', 'rimdiamter', 'loadindex', 'speedsymbol', 'warranty_summery', 'left_image', 'right_image', 'front_image', 'back_image', 'mrp', 'name', 'brand')
