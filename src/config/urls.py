from django.contrib import admin
from django.urls import path, include
from apps.books.views import BooksView
from apps.users.views import UsersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', BooksView.as_view()),
    path('api/books/<int:pk>', BooksView.as_view()),
    path('api/users/', UsersView.as_view())
]
