from rest_framework import serializers
from website.models import Grandeur, Mesure

class GrandeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grandeur
        fields = '__all__'

class MesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesure
        fields=['valeur','datePrise','grandeur']