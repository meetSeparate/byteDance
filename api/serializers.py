from rest_framework import serializers
from api.models import UserInfo, Product, Category, City, Job


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    city_name = serializers.CharField(source='city.name', read_only=True)
    recruit_type = serializers.CharField(source='recruit_type.type', read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
