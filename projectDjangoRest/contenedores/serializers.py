from rest_framework import serializers

class ContenedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenedor
        fields = '__all__'
