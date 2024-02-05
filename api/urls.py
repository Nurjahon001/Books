from django.urls import path
from .views import BookReviewAPIView,CustomUserAPIView,CustomUserDetailAPIView,BookListAPIView,BookDetailAPIView,BookReviewDetailAPIView

app_name = 'api'
urlpatterns=[
    path('book-reviews/',BookReviewAPIView.as_view(), name='book-reviews'),
    path('book-reviews/<int:pk>/', BookReviewDetailAPIView.as_view(), name='book-review-detail'),
    path('book-list/', BookListAPIView.as_view(), name='book-list'),
    path('book-list/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('users/', CustomUserAPIView.as_view(), name='users'),
    path('users/<int:pk>/', CustomUserDetailAPIView.as_view(), name='users-detail'),
]