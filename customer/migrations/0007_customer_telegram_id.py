# Generated by Django 5.1.2 on 2024-11-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_rename_location_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='telegram_id',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True),
        ),
    ]
