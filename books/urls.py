# from django.urls import path
# # from .views import get_list_phone, get_phone_info
# from .views import ListBook, BookDetail
#
# urlpatterns = [
#     # path('', get_list_phone, name='list-phone'),
#     # path('<int:pk>/', get_phone_info, name='detail-phone')
#     path('', ListBook.as_view(), name='list-book'),
#     path('<int:pk>/', BookDetail.as_view(), name='detail-book')
# ]