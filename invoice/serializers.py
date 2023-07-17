from rest_framework import serializers
from .models import Invoice, InvoiceDetail


class InvoiceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceDetail
        fields = ('description', 'quantity', 'unit_price', 'price')

class InvoiceListSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ('id', 'date', 'invoice_number', 'customer_name', 'details')
    
    def get_details(self, invoice):
        details = invoice.invoicedetail_set.all()
        serializer = InvoiceDetailSerializer(details, many=True)
        return serializer.data

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, write_only=True)

    class Meta:
        model = Invoice
        fields = ('id', 'date', 'invoice_number', 'customer_name', 'details')

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice
