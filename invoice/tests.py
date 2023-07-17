from django.urls import reverse
from datetime import date
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Invoice, InvoiceDetail


class InvoiceTests(APITestCase):
    def setUp(self):
        self.invoice_data = {
            'date': '2023-07-17',
            'invoice_number': 1,
            'customer_name': 'John Doe',
            'details': [
                {
                    'description': 'Item A',
                    'quantity': 2,
                    'unit_price': 10.00,
                    'price': 20.00
                },
                {
                    'description': 'Item B',
                    'quantity': 3,
                    'unit_price': 5.00,
                    'price': 15.00
                }
            ]
        }

        self.invoice = Invoice.objects.create(
            date='2023-07-17',
            invoice_number=1,
            customer_name='John Doe'
        )
        InvoiceDetail.objects.create(
            invoice=self.invoice,
            description='Item A',
            quantity=2,
            unit_price=10.00,
            price=20.00
        )
        InvoiceDetail.objects.create(
            invoice=self.invoice,
            description='Item B',
            quantity=3,
            unit_price=5.00,
            price=15.00
        )

    def test_create_invoice(self):
        url = reverse('invoice-list')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)
        self.assertEqual(InvoiceDetail.objects.count(), 4)

    def test_get_invoice_list(self):
        url = reverse('invoice-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['invoice_number'], 1)
        self.assertEqual(len(response.data[0]['details']), 2)

    def test_get_invoice_detail(self):
        url = reverse('invoice-detail', args=[self.invoice.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['invoice_number'], 1)
        self.assertEqual(len(response.data['details']), 2)

    def test_update_invoice(self):
        url = reverse('invoice-detail', args=[self.invoice.id])
        updated_data = {
            'date': date.today().isoformat(),
            'invoice_number': 2,
            'customer_name': 'Jane Smith',
            'details': [
                {
                    'description': 'Item C',
                    'quantity': 1,
                    'unit_price': 15.00,
                    'price': 15.00
                },
                {
                    'description': 'Item D',
                    'quantity': 4,
                    'unit_price': 8.00,
                    'price': 32.00
                }
            ]
        }
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice.refresh_from_db()
        self.assertEqual(str(self.invoice.date), updated_data['date'])
        self.assertEqual(self.invoice.invoice_number, 2)
        self.assertEqual(self.invoice.customer_name, 'Jane Smith')
        self.assertEqual(self.invoice.invoicedetail_set.count(), 2)

    def test_delete_invoice(self):
        url = reverse('invoice-detail', args=[self.invoice.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)
        self.assertEqual(InvoiceDetail.objects.count(), 0)
