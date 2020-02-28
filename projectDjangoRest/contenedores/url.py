from django.urls import path
from rest_framework.routers import DefaultRouter

from contenedores.apiviews import ContenedorViewSet

router = DefaultRouter()
router.register('v2/contenedores', ContenedorViewSet, basename='contenedores')