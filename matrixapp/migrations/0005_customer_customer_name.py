# Generated by Django 4.0.2 on 2022-05-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0004_alter_customer_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]