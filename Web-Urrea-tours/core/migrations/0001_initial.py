# Generated by Django 2.2 on 2019-05-17 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPrincipalInicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=100, verbose_name='SubTitulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('NameBtn', models.CharField(default='Haz click aquí', max_length=30, verbose_name='Nombre del boton')),
                ('url', models.URLField(blank=True, max_length=500, null=True, verbose_name='Enlace')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now_add=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'Cambiar Texto Banner Principal',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Banners', max_length=30, verbose_name='Banners')),
                ('bannerInicio', models.ImageField(blank=True, null=True, upload_to='banners', verbose_name='Banner Inicio')),
                ('bannerBlog', models.ImageField(blank=True, null=True, upload_to='banners', verbose_name='Banner Blog')),
                ('bannerAbout', models.ImageField(blank=True, null=True, upload_to='banners', verbose_name='Banner Otros')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now_add=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'Cambiar Banner',
                'ordering': ['-created'],
            },
        ),
    ]
