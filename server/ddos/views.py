from rest_framework.viewsets import ModelViewSet

from .models import Site, Proxy
from .serializers import SiteSerializer, ProxySerializer
from .filters import SiteFilterSet


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filterset_class = SiteFilterSet


class ProxyViewSet(ModelViewSet):
    queryset = Proxy.objects.all()
    serializer_class = ProxySerializer
    filterset_fields = ('status',)
