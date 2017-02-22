from rest_framework.permissions import BasePermission

class UserPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return request.method == 'GET'
