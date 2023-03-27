from rest_framework import permissions

from .choices import VIA_EMAIL, VIA_PHONE_NUMBER


class IsRegisteredViaPhoneNumber(permissions.BasePermission):
    """
    Check if user's auth type is VIA_PHONE_NUMBER
    """

    def has_permission(self, request, view):

        return bool(
            request.user and request.user.is_authenticated and
            request.user.auth_type == VIA_PHONE_NUMBER
        )


class IsRegisteredViaEmail(permissions.BasePermission):
    """
    Check if user's auth type is VIA_EMAIL
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and
            request.user.auth_type == VIA_EMAIL
        )
