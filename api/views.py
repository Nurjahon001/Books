from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import BookReviewSerializer, CustomUserSerializer,BooksSerializer
from books.models import BookReview,Books
from users.models import CustomUser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from api.book.formats import format_books
# Create your views here.

class BookListGenericView(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):
        books=Books.objects.all().order_by('-create_at')
        try:
            books=[format_books(book) for book in books]
            ctx={
                'ctx':books
            }
            return Response(ctx,status=200)
        except Exception as e:
            return Response(f'Kitoblar mavjud emas\n{e}',status=400)
    def delete(self,request,pk,*args,**kwargs):
        try:
            book=Books.objects.get(pk=pk)
            book.delete()
            return  Response('Ochirildi',status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f'Bunaqa id da kitob yoq',status=status.HTTP_400_BAD_REQUEST)

# class BookReviewCRUD(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated, ]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all().order_by("-create_at")
#     lookup_field = "pk"

# class BookReviewListAPIView(generics.ListCreateAPIView):
#     serializer_class=BookReviewSerializer
#     queryset=BookReview.objects.all().order_by("-create_at")
#     lookup_field="pk"

# class BookReviewListAPIView(APIView):
#     def get(self,request):
#         book_review=BookReview.objects.all()
#         paginator=PageNumberPagination()
#         page_obj=paginator.paginate_queryset(book_review,request)
#         serializer=BookReviewSerializer(page_obj,many=True)
#         return paginator.get_paginated_response(data=serializer.data)
#
#     def post(self,request):
#         serializer=BookReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class BookReviewDetailUpdateDelateAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated,]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all()
#     lookup_field = "pk"

class BookReviewDetailUpdateDelateAPIView(APIView):
    def get(self,request,pk):
        book_review=BookReview.objects.get(pk=pk)
        serializer=BookReviewSerializer(book_review)
        return Response(data=serializer.data)

    def delete(self,request,pk):
        book_review=BookReview.objects.get(pk=pk)
        book_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        book_review = BookReview.objects.get(pk=pk)
        serializer=BookReviewSerializer(instance=book_review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        book_review = BookReview.objects.get(pk=pk)
        serializer=BookReviewSerializer(instance=book_review,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class BookListAPIView(APIView):
#     def get(self,request):
#         books=Books.objects.all()
#         serializer=BooksSerializer(books,many=True)
#         return Response(data=serializer.data)
#
#
# class BookDetailAPIView(APIView):
#     def get(self,request,pk):
#         book=Books.objects.get(pk=pk)
#         serializer=BooksSerializer(book)
#         return Response(data=serializer.data)
#
#
# class CustomUserListAPIView(APIView):
#     def get(self,request):
#         user=CustomUser.objects.all()
#         serializer=CustomUserSerializer(user,many=True)
#         return Response(data=serializer.data)
#
#
# class CustomUserDetailAPIView(APIView):
#     def get(self,request,pk):
#         user=CustomUser.objects.get(pk=pk)
#         serializer=CustomUserSerializer(user)
#         return Response(data=serializer.data)


