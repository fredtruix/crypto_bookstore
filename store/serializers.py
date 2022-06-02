from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (Categories, Chapter, User, Book, Wishlist, checkout, Referal, UserBooks, Withdrawer)


class UserSerializer(ModelSerializer):
    password = serializers.CharField(
        max_length=64, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email', ('email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ['id','author','author_name','Book_image', 'book_name','overview','description','category_name', 'categories', 'price', 'strike_price',
                  'likes', 'rating', 'date_created','date_update']


class ChapterSerializer(ModelSerializer):

    class Meta:
        model = Chapter
        fields = ['id', 'owner', 'book_ref', 'booK_name', 'chapter_name', 'Chapter_title', 'book_text', 'date_created']


class CategoriesSerializer(ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'user_image', 'username','first_name','last_name', 'email', 'bio',
                  'amount', 'address', 'linkedIn', 'twitter', 'instagram']


class CheckOutSerializer(ModelSerializer):

    class Meta:
        model = checkout
        fields = ['id', 'owner', 'books', 'total_amount']


class UserBookSerializer(ModelSerializer):

    class Meta:
        model = UserBooks
        fields = ['id', 'owner', 'books']



class wishListSerializer(ModelSerializer):

    class Meta:
        model = Wishlist
        fields = ['owner', 'books']



class ReferalSerializer(ModelSerializer):

    class Meta:
        model = Referal
        fields = ['id','owner', 'users']



class WithdrawerSerializer(ModelSerializer):

    class Meta:
        model = Withdrawer
        fields = "__all__"


