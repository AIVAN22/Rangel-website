# Generated by Django 4.0.4 on 2023-04-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rangel_portfolio', '0010_alter_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='canvas',
            field=models.CharField(choices=[('canvas1', 'canvas1'), ('canvas2', 'canvas2'), ('canvas3', 'canvas3')], default=1, max_length=350),
        ),
    ]
