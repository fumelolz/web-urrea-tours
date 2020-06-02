# Generated by Django 2.2 on 2019-05-19 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='subtitle',
            field=models.CharField(max_length=100, verbose_name='Subtitulo Motivador'),
        ),
    ]