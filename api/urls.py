from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import take_category, save_photo, start_neuron

router = SimpleRouter()

# router.register(r'photo', PhotoViewSet)


urlpatterns = [
    path('categories/', take_category),
    path('save_photo/', save_photo),
    path('start_neuron/', start_neuron),
]
