from rest_framework import serializers
from core.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','nombre','precio', 'img', 'caracteristicas','categoria']

#user
class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.nombre = validate_data.get('nombre')
        instance.apellido = validate_data.get('apellido')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.password = validate_data.get('password')

    def validate_username(self,data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe ingrese uno nuevo")
        else:
            return data