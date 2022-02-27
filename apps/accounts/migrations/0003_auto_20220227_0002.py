# Generated by Django 2.2.2 on 2022-02-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220226_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicuserprofile',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='basicuserprofile',
            name='dateofbirth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='basicuserprofile',
            name='gender',
            field=models.CharField(default='male', max_length=20),
        ),
    ]
