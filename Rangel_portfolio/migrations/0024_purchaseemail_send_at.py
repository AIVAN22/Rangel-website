# Generated by Django 4.2.4 on 2024-02-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rangel_portfolio', '0023_purchaseemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseemail',
            name='send_at',
            field=models.DateTimeField(null=True, verbose_name='Received_At'),
        ),
    ]