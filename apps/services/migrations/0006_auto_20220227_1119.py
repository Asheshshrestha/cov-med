# Generated by Django 2.2.2 on 2022-02-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20220224_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalservicemodule',
            name='is_ineffect',
            field=models.BooleanField(default=True),
        ),
    ]
