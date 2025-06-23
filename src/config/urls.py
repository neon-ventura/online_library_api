from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.books.views import BookViewSet
from apps.users.views import UserViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]