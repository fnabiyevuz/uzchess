from django.urls import path
from rest_framework.authtoken import views
from apps.users.api_endpoints import registration, login, profile, change_phone_number, change_email, reset_password

app_name = "users"

urlpatterns = [
    # REGISTRATION
    path(
        "register/send-verification-code/",
        registration.SendVerificationCodeAPIView.as_view(),
        name="register-send-verification-code",
    ),
    path("register/verify-code/", registration.VerifyCodeAPIView.as_view(), name="register-verify-code"),
    path("register/set-password/", registration.SetPasswordAPIView.as_view(), name="register-set-password"),

    # LOGIN
    path('login/', views.obtain_auth_token, name='login-username-password'),
    path("login/google/", login.GoogleLogin.as_view(), name='google-login'),

    # RESET PASSWORD
    path('reset-password/send-code/', reset_password.SendCodeAPIView.as_view(), name='send-reset-password-send-code'),
    path('reset-password/verify-code/', reset_password.VerifyCodeAPIView.as_view(), name='verify-reset-password-code'),
    path('reset-password/', reset_password.ResetPasswordAPIView.as_view(), name='reset-password'),

    # PROFILE
    path('profile/detail/', profile.GetProfileAPIView.as_view(), name='get-profile'),
    path('profile/update/', profile.UpdateProfileAPIView.as_view(), name='update-profile'),
    path('profile/change-password/', profile.ChangePasswordAPIView.as_view(), name='change-password'),
    # favourite items
    path('profile/favourite-books/', profile.GetFavouriteBooksAPIView.as_view(), name='favourite-books'),
    # orders
    path('profile/orders/', profile.GetOrdersListAPIView.as_view(), name='profile-orders'),

    # CHANGE PHONE NUMBER OR EMAIL
    # phone number
    path(
        'profile/change-phone-number/send-verification-code/',
        change_phone_number.SendVerificationCodeAPIView.as_view(),
        name='change-phone-number-send-verification-code'
    ),
    path(
        'profile/change-phone-number/verify-code/',
        change_phone_number.VerifyCodeAPIView.as_view(),
        name='change-phone-number-verify-code'
    ),
    # email
    path(
        'profile/change-email/send-verification-code/',
        change_email.SendVerificationCodeAPIView.as_view(),
        name='change-email-send-verification-code'
    ),
    path(
        'profile/change-email/verify-code/',
        change_email.VerifyCodeAPIView.as_view(),
        name='change-email-verify-code'
    ),

]
