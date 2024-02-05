from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import BookReviewSerializer, CustomUserSerializer,BooksSerializer
from books.models import BookReview,Books
from users.models import CustomUser
# Create your views here.
class BookReviewAPIView(APIView):
    def get(self,request):
        books=BookReview.objects.all()
        serializer=BookReviewSerializer(books,many=True)
        return Response(data=serializer.data)


class BookReviewDetailAPIView(APIView):
    def get(self,request,pk):
        books=BookReview.objects.get(pk=pk)
        serializer=BookReviewSerializer(books)
        return Response(data=serializer.data)


class BookListAPIView(APIView):
    def get(self,request):
        books=Books.objects.all()
        serializer=BooksSerializer(books,many=True)
        return Response(data=serializer.data)


class BookDetailAPIView(APIView):
    def get(self,request,pk):
        book=Books.objects.get(pk=pk)
        serializer=BooksSerializer(book)
        return Response(data=serializer.data)


class CustomUserAPIView(APIView):
    def get(self,request):
        user=CustomUser.objects.all()
        serializer=CustomUserSerializer(user,many=True)
        return Response(data=serializer.data)


class CustomUserDetailAPIView(APIView):
    def get(self,request,pk):
        user=CustomUser.objects.get(pk=pk)
        serializer=CustomUserSerializer(user)
        return Response(data=serializer.data)