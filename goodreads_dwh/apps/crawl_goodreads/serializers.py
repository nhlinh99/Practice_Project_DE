from rest_framework import serializers
from .models import Information_Book_Detail, Information_User_Detail, User_Rating_Information


class Information_Book_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Information_Book_Detail
        fields = '__all__'


class Information_User_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Information_User_Detail
        fields = '__all__'


class User_Rating_Information_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Rating_Information
        fields = '__all__'