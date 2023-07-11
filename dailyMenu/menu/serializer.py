import datetime

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Menu, Order
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'title', 'description', 'days', 'price')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        now = datetime.datetime.now()
        day = now.strftime("%a")
        Order.objects.create(user_id=user.id, day=day)
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('dish', )

    def create(self, validated_data):
        order = Order.objects.create(user_id=self.context["user_id"], dish_id=validated_data['dish'])
        return order

    def update(self, instance, validated_data):
        print(instance.day)
        instance.dish = validated_data.get("dish", instance.dish)
        print(validated_data.get("dish", instance.dish))
        instance.save()
        return instance

class DailyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
