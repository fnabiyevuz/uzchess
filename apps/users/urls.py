from django.urls import path, include
from rest_framework.authtoken import views
from apps.users.api_endpoints import registration, login

app_name = "users"

urlpatterns = [
    path(
        "register/send-verification-code/",
        registration.SendVerificationCodeAPIView.as_view(),
        name="register-send-verification-code",
    ),
    path("register/verify-code/", registration.VerifyCodeAPIView.as_view(), name="register-verify-code"),
    path("register/set-password/", registration.SetPasswordAPIView.as_view(), name="register-set-password"),

    path('login/', views.obtain_auth_token, name='login-username-password'),

    path("login/google/", login.GoogleLogin.as_view(), name='google-login'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

]
