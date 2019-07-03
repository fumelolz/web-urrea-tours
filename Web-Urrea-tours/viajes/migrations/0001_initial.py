# Generated by Django 2.2 on 2019-06-27 20:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=100, verbose_name='Nombre Del Destino')),
                ('descripcion', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='paquetes', verbose_name='Imagen')),
                ('precio', models.DecimalField(decimal_places=10, default=0.0, max_digits=19, verbose_name='Precio del destino')),
                ('published', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha del viaje')),
            ],
        ),
        migrations.CreateModel(
            name='NoIncluye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noIncluye', models.CharField(max_length=100, verbose_name='No Incluye')),
                ('paquete', models.ForeignKey(default='Vacio', on_delete=django.db.models.deletion.CASCADE, related_name='noinc', to='viajes.Paquete', verbose_name='Cosas que incluye')),
            ],
        ),
        migrations.CreateModel(
            name='Incluye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incluye', models.CharField(max_length=100, verbose_name='Incluye')),
                ('paquete', models.ForeignKey(default='Vacio', on_delete=django.db.models.deletion.CASCADE, related_name='inc', to='viajes.Paquete', verbose_name='Cosas que incluye')),
            ],
        ),
    ]
