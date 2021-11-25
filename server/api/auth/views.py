from djoser.views import TokenCreateView as BaseTokenCreateView, TokenDestroyView as BaseTokenDestroyView
from djoser.serializers import TokenSerializer
from drf_spectacular.utils import extend_schema


class TokenCreateView(BaseTokenCreateView):
    # Fix response schema
    @extend_schema(
        responses={200: TokenSerializer},
    )
    def post(self, request, **kwargs):
        return super().post(request, **kwargs)


class TokenDestroyView(BaseTokenDestroyView):
    pass
