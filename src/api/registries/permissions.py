from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    
    message = 'You are not the owner of this registry.'

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS and obj.user == request.user