from .views import BookReviewCRUD
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('reviews', BookReviewCRUD, basename='reviews')
urlpatterns = router.urls


# from django.urls import path
# from .views import BookReviewListAPIView,CustomUserListAPIView,CustomUserDetailAPIView,BookListAPIView,BookDetailAPIView,BookReviewDetailUpdateDelateAPIView
#
# app_name = 'api'
# urlpatterns=[
#     path('reviews/',BookReviewListAPIView.as_view(), name='reviews'),
#     path('reviews/<int:pk>/', BookReviewDetailUpdateDelateAPIView.as_view(), name='delate-update-detail'),
#     path('book-list/', BookListAPIView.as_view(), name='book-list'),
#     path('book-list/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
#     path('users/', CustomUserListAPIView.as_view(), name='users'),
#     path('users/<int:pk>/', CustomUserDetailAPIView.as_view(), name='users-detail'),
# ]