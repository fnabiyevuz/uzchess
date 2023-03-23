from django.urls import path

from apps.users.api_endpoints import registration

app_name = "users"

urlpatterns = [
    # path(),
    path(
        "register/send-verification-code/",
        registration.SendVerificationCodeAPIView.as_view(),
        name="register-send-verification-code",
    ),
    path("register/verify-code/", registration.VerifyCodeAPIView.as_view(), name="register-verify-code"),
    path("register/set-password/", registration.SetPasswordAPIView.as_view(), name="register-set-password"),
]
