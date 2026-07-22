from rest_framework.permissions import BasePermission

def has_user_type(user, user_type):
  if not user.is_authenticated:
    return False
  return user.user_type >= user_type
    
class IsStudentAndOwnsObject(BasePermission):
  def has_object_permission(self, request, view, obj):
    return has_user_type(request.user, 0) and obj.user == request.user
    
class IsAdminOrOwner(BasePermission):
  def has_object_permission(self, request, view, obj):
    return (
      has_user_type(request.user, 1)
      or obj.user == request.user
    )

class IsAdmin(BasePermission):
  def has_permission(self, request, view):
    return has_user_type(request.user, 1)