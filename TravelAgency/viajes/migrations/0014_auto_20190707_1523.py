# Generated by Django 2.2 on 2019-07-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0013_auto_20190707_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='doble',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=19, null=True, verbose_name='Precio doble'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='extradoble',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=19, null=True, verbose_name='Precio Noche extra doble'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='extraniños',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=19, null=True, verbose_name='Precio noche extra niños'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='extrasencilla',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=19, null=True, verbose_name='Precio Noche extra sencilla'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='extratriple',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=19, null=True, verbose_name='Precio Noche extra triple'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='niños',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=19, null=True, verbose_name='Precio niños'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='sencilla',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=19, null=True, verbose_name='Precio sencilla'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='triple',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=19, null=True, verbose_name='Precio triple'),
        ),
    ]