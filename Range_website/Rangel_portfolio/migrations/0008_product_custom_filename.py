# Generated by Django 4.1.5 on 2023-01-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Rangel_portfolio", "0007_alter_product_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="custom_filename",
            field=models.CharField(default="default", max_length=250),
        ),
    ]
