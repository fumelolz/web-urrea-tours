# Generated by Django 2.2 on 2019-07-07 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0008_auto_20190706_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquete',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='paquete',
            name='published',
        ),
    ]
