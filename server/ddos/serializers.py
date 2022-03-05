from rest_framework import serializers

from .models import Site, Proxy


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = (
            'id',
            'url',
            'date_created',
            'date_updated',
        )


class ProxySerializer(serializers.ModelSerializer):
    host = serializers.CharField(read_only=True)
    url = serializers.CharField(read_only=True)
    country = serializers.SlugRelatedField(slug_field='code', read_only=True)

    class Meta:
        model = Proxy
        fields = (
            'id',
            'ip',
            'http_port',
            'https_port',
            'socks_port',
            'username',
            'password',
            'host',
            'url',
            'country',
            'status',
            'speed',
            'is_active',
            'date_created',
            'date_updated',
        )
