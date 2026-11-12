from rest_framework import serializers
from .models import Usuario, Cliente


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = Usuario
        fields = [
            "id", "username", "first_name", "last_name", "email",
            "is_active", "is_staff", "date_joined", "password",
        ]
        read_only_fields = ["date_joined"]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        usuario = Usuario(**validated_data)
        if password:
            usuario.set_password(password)
        else:
            usuario.set_unusable_password()
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for atributo, valor in validated_data.items():
            setattr(instance, atributo, valor)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
