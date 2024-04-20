from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    balance = serializers.FloatField()
    class Meta:
        model = Account
        fields = '__all__'