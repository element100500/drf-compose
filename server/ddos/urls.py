from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()

router.register('sites', views.SiteViewSet)
router.register('proxies', views.ProxyViewSet)

urlpatterns = router.urls
