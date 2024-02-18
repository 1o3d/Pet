from rest_framework import serializers
from main_app.models import historicalModels

class historicalSerializers(serializers.Serializer):
    class Meta:
        model = historicalModels
        fields = '__all__'
        