# Generated by Django 4.2.8 on 2024-01-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=100)),
                ('expired', models.BooleanField(default=False)),
                ('discount_price', models.PositiveIntegerField(default=100)),
                ('minimum_amount', models.PositiveIntegerField(default=500)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]