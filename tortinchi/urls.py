from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tortinchi.views import (Salom1vset, Salom2vset, Salom3vset, Salom4vset, Salom5vset)



router = DefaultRouter()
router.register(r"1", Salom1vset, basename="salom1")
router.register(r"2", Salom2vset, basename="salom2")
router.register(r"3", Salom3vset, basename="salom3")
router.register(r"4", Salom4vset, basename="salom4")
router.register(r"5", Salom5vset, basename="salom5")



urlpatterns = [
    path("", include(router.urls)),
]