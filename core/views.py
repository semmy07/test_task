from rest_framework import viewsets
from rest_framework.permissions import AllowAny
# from rest_framework.views import APIView

from core.models import Contact
from core.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = (AllowAny,)
