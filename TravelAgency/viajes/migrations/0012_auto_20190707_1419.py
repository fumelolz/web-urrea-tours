# Generated by Django 2.2 on 2019-07-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0011_plan_temporada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='categoriaHotel',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='1 a 5'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='doble',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True, verbose_name='Precio doble'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='extradoble',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True, verbose_name='Precio Noche extra doble'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='extraniños',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True, verbose_name='Precio noche extra niños'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='extrasencilla',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True, verbose_name='Precio Noche extra sencilla'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='extratriple',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True, verbose_name='Precio Noche extra triple'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='niños',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True, verbose_name='Precio niños'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre del plan'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='sencilla',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True, verbose_name='Precio sencilla'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='triple',
            field=models.DecimalField(decimal_places=4, max_digits=19, null=True, verbose_name='Precio triple'),
        ),
    ]
