# Generated by Django 4.0.3 on 2022-04-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overseasApp', '0007_alter_invoice_order_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Date',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
