from rest_framework import serializers
from .models import FacebookUser

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookUser
        fields = ['id','email','phone','is_email','cookie']
    