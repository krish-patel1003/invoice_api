# Generated by Django 4.2.3 on 2023-07-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_alter_invoicedetail_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
