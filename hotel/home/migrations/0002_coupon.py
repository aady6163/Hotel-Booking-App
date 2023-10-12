# Generated by Django 3.0.5 on 2023-09-30 09:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('uplaoded_at', models.DateField(auto_now_add=True)),
                ('coupon_name', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]