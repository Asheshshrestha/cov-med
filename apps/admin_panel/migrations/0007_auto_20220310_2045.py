# Generated by Django 2.2.2 on 2022-03-10 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_websitesettingmodel_show_website_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='websitesettingmodel',
            options={'permissions': (('view_dashboard', 'Can View Dashboard'),)},
        ),
    ]
