from django.urls import path, include
from .views import Books


urlpatterns = [
    path('', Books.as_view())
]
