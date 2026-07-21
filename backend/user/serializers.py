from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  role_display = serializers.SerializerMethodField()
  full_name = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ["id", "full_name", "email", "role_display"]
    read_only_fields = ["id", "email", "role_display"]

  def get_role_display(self, obj):
    return obj.get_role_display()
  
  def get_full_name(self, obj):
    return f"{obj.first_name} {obj.last_name}"
  
