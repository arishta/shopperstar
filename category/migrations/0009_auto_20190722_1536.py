# Generated by Django 2.2.3 on 2019-07-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_auto_20190722_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price_currency',
        ),
        migrations.AddField(
            model_name='products',
            name='currency',
            field=models.CharField(choices=[('₹', 'INR'), ('$', 'USD')], default='₹', max_length=3),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
