# serializers.py


from rest_framework import serializers

from .models import MusicSample, SampleCategory, Order, SampleReview, CartItem, Visit
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class MusicSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicSample
        fields = '__all__'


class SampleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleCategory
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class SampleReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleReview
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
