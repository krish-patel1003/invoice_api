from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer, InvoiceListSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return InvoiceListSerializer
        return super().get_serializer_class()
