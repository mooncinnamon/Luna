from django.shortcuts import render
from rest_framework import viewsets
from .serializer import HostsSerializer
from .models import Hosts


# Create your views here.
class HostsView(viewsets.ModelViewSet):
    serializer_class = HostsSerializer
    queryset = Hosts.objects.all()
