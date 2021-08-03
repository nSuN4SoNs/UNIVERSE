from django.urls import path, include
from rest_framework.routers import DefaultRouter
from car.api.views import CompanyViewSet

router = DefaultRouter()

router.register("companies", CompanyViewSet)

urlpatterns = [
    path("", include(router.urls))
]
