from django.urls import path, include
from .views import Books


urlpatterns = [
    path('', Books.as_view(), name='book_list'),
    path('<int:pk>/', Books.as_view(), name='book_params')
]
