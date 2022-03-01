# Generated by Django 2.2.2 on 2022-02-28 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20220227_1159'),
        ('accounts', '0008_auto_20220228_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicuserprofile',
            name='doctor_regestriation_no',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='basicuserprofile',
            name='hospital',
        ),
        migrations.AddField(
            model_name='basicuserprofile',
            name='hospital',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.HospitalModel'),
        ),
        migrations.AlterField(
            model_name='basicuserprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
