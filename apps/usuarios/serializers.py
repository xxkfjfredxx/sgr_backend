from rest_framework import serializers
from .models import UserRole, User


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class UserSerializer(serializers.ModelSerializer):
    role = UserRoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=UserRole.objects.all(),
        source="role",  # este es el campo real del modelo
        write_only=True,
    )
    employee_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_superuser",
            "is_staff",
            "role",  # se devuelve como objeto
            "role_id",  # se usa para crear/editar
            "employee_id",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
        }

    def get_employee_id(self, obj):
        return getattr(getattr(obj, "employee", None), "id", None)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data.pop("password"))
        return super().update(instance, validated_data)
