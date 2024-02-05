from rest_framework import serializers
from books.models import BookReview,Books
from users.models import CustomUser

class BookReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    book = serializers.CharField()

    class Meta:
        model = BookReview
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


# class BookListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Books
#         # fields = ['title', 'description', 'isbn', 'price']


