from django.shortcuts import render

# Create your views here.

from .models import Contact, ContactInfo
from .serializers import ContactSerializer, ContactInfoSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
# Create your views here.


class ContactInfoView(ListAPIView):
    queryset = ContactInfo.objects.all().order_by('-id')[:1]
    serializer_class = ContactInfoSerializer


class ContactView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer