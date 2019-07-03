# Generated by Django 2.2 on 2019-06-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Subtitulo Motivador')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now_add=True, verbose_name='Fecha de edición')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='paquete',
            name='precio',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19, verbose_name='Precio del destino'),
        ),
        migrations.AddField(
            model_name='paquete',
            name='categories',
            field=models.ManyToManyField(related_name='get_tipo', to='viajes.Categoria', verbose_name='Categorías'),
        ),
    ]
