# Generated by Django 4.2.4 on 2024-02-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rangel_portfolio', '0026_uploadimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimages',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]