from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token-auth', obtain_auth_token, name="accounts.token_auth")
]