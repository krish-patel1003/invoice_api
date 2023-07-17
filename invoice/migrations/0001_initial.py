# Generated by Django 4.2.3 on 2023-07-17 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('invoice_number', models.IntegerField()),
                ('customer_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
            ],
        ),
    ]
