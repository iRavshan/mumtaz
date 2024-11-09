# Generated by Django 5.1.2 on 2024-10-24 19:37

import common.generators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courier', '0001_initial'),
        ('customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('key', models.CharField(auto_created=True, default=common.generators.order_key_generator, editable=False, max_length=10, unique=True)),
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('replacement_bottles', models.PositiveSmallIntegerField(default=0)),
                ('new_bottles', models.PositiveSmallIntegerField(default=0)),
                ('location', models.CharField(max_length=200)),
                ('geo_location', models.URLField(blank=True, null=True)),
                ('received_at', models.DateTimeField(null=True)),
                ('delivered_at', models.DateTimeField(null=True)),
                ('asap_delivery', models.BooleanField(default=True)),
                ('preferred_delivery_datetime', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('new', 'Yangi'), ('received', 'Qabul qilingan'), ('delivering', 'Yetkazilmoqda'), ('delivered', 'Yetkazilgan'), ('cancelled', 'Bekor qilingan')], default='new', max_length=20)),
                ('courier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courier.courier')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('received_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
