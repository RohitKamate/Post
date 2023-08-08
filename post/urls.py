"""URLs for job API"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post import views



router = DefaultRouter()


app_name = "post"
router.register("post", views.PostViewSet)


urlpatterns = [
    path("", include(router.urls))
]