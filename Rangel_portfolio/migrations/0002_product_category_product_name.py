# Generated by Django 4.1.5 on 2023-01-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Rangel_portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=350, null=True),
        ),
    ]
