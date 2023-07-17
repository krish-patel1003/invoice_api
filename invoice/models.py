from django.db import models

# Create your models here.

class Invoice(models.Model):

    date = models.DateField(auto_created=True)
    invoice_number = models.IntegerField()
    customer_number = models.IntegerField()


class InvoiceDetail(models.Model):

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    