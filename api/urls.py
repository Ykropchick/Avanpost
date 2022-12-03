from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import take_category, take_photo

router = SimpleRouter()

# router.register(r'photo', PhotoViewSet)


urlpatterns = [
    path('test/', take_category),
    path('photo/', take_photo)
]
