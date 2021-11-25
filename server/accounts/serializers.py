from rest_framework.serializers import CharField
from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.conf import settings as djoser_settings


User = get_user_model()


class UserSerializer(BaseUserSerializer):
    full_name = CharField(read_only=True, source='get_full_name')

    class Meta(BaseUserSerializer.Meta):
        fields = (
            djoser_settings.USER_ID_FIELD,
            djoser_settings.LOGIN_FIELD,
        ) + tuple(User.REQUIRED_FIELDS) + (
            'first_name',
            'last_name',
            'full_name',
        )
