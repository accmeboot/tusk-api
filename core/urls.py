from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


from utils.get_api_url import get_api_url

urlpatterns = [
    path("admin/", admin.site.urls),
    path(get_api_url("users"), include("users.urls")),
    path(get_api_url("projects"), include("projects.urls")),
    path(get_api_url("tasks"), include("tasks.urls")),
    path(get_api_url("labels"), include("labels.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            get_api_url("schema"),
            SpectacularAPIView.as_view(),
            name="schema",
        ),
        path(
            get_api_url("docs"),
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
