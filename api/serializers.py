from rest_framework import serializers
from books.models import BookReview,Books
from users.models import CustomUser




class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class BookReviewSerializer(serializers.ModelSerializer):
    user=CustomUserSerializer(read_only=True)
    book=BooksSerializer(read_only=True)
    user_id=serializers.IntegerField(write_only=True)
    book_id=serializers.IntegerField(write_only=True)
    class Meta:
        model = BookReview
        fields = ['comment','star_given','user','book','user_id','book_id']


