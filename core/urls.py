from django.contrib import admin
from django.urls import include, path

from utils.get_api_url import get_api_url

urlpatterns = [
    path("admin/", admin.site.urls),
    path(get_api_url("users"), include("users.urls")),
]
