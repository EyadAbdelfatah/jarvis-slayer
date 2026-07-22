from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
  role_display = serializers.SerializerMethodField()
  full_name = serializers.SerializerMethodField()

  class Meta:
    model = CustomUser
    fields = ["id", "full_name", "email", "role_display"]
    read_only_fields = ["id", "is_staff", "is_superuser", "email", "role"]

  def get_role_display(self, obj):
    return obj.get_role_display()
  
  def get_full_name(self, obj):
    return f"{obj.first_name} {obj.last_name}"
  
class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only=True
  )

  class Meta:
    model = CustomUser
    fields = [
      "email",
      "password",
      "first_name",
      "last_name",
    ]

  def create(self, validated_data):
    validated_data["role"] = 0
    return CustomUser.objects.create_user(
        **validated_data
    )