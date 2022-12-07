from rest_framework.routers import DefaultRouter

from labels.views import LabelsViewSet


router = DefaultRouter()
router.register("", LabelsViewSet, basename="labels")

urlpatterns = router.urls
