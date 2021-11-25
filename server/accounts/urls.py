from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()

router.register('users', views.UserViewSet)
# router.register('another', views.AnotherViewSet)

urlpatterns = router.urls
