from dataclasses import fields
from rest_framework import serializers

from cnab.models import Cnab

class CnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields = '__all__'