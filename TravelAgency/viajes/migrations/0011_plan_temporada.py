# Generated by Django 2.2 on 2019-07-07 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0010_auto_20190707_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del paquete')),
                ('hotel', models.CharField(max_length=100, verbose_name='Hotel')),
                ('categoriaHotel', models.PositiveSmallIntegerField(verbose_name='1 a 5')),
                ('sencilla', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='Precio sencilla')),
                ('extrasencilla', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='Precio Noche extra sencilla')),
                ('doble', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='Precio doble')),
                ('extradoble', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='Precio Noche extra doble')),
                ('triple', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='Precio triple')),
                ('extratriple', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='Precio Noche extra triple')),
                ('niños', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='Precio niños')),
                ('extraniños', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='Precio noche extra niños')),
                ('paquete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_paquete', to='viajes.Paquete')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='viajes.Temporada')),
            ],
        ),
    ]
