from django.db import models

# Create your models here.

class Invoice(models.Model):

    date = models.DateField(auto_now_add=True)
    invoice_number = models.IntegerField()
    customer_name = models.CharField(max_length=100)


class InvoiceDetail(models.Model):

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

