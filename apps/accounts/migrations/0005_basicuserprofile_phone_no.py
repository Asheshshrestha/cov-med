# Generated by Django 2.2.2 on 2022-02-27 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220227_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicuserprofile',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
