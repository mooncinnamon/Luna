from rest_framework import serializers
from .models import Hosts


class HostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hosts
        fields = '__all__'
