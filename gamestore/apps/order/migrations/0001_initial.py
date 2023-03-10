# Generated by Django 4.1.6 on 2023-02-09 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_method', models.CharField(choices=[('credit_card', 'CREDIT_CARD'), ('debit_card', 'DEBIT_CARD'), ('paypal', 'PAYPAL'), ('pix', 'PIX')], max_length=100)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('items', models.ManyToManyField(related_name='orders', to='catalog.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
