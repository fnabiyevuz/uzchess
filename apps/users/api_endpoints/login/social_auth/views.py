from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from allauth.account.adapter import get_adapter
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "80648852248-b62n2o3g3noiigl64jn094l4aqtkbc8m.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/api/v1/users/login/google/'
    client_class = OAuth2Client


__all__ = ['GoogleLogin']
