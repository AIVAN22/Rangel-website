# Generated by Django 4.1.5 on 2023-01-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Rangel_portfolio", "0008_product_custom_filename"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="img",
            field=models.ImageField(
                default="static/images/default.jpg", upload_to="images/"
            ),
        ),
    ]
