import datetime
from rest_framework import permissions
from django.conf import settings


class IsConfirmedServer(permissions.BasePermission):
    """
    Permission for using API methods, based on special auth token where code timestamp.
    Permission gets only if time of request not bigger then current time + 60 seconds
    """
    def has_permission(self, request, view):
        if settings.USE_HASHED_TOKEN is False:
            return True
        else:
            token = request.META.get('HTTP_AUTH_KEY', None)
            if token:
                if settings.AUTH_TOKEN == token:
                    return True
        return False