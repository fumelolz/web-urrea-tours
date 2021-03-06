# Generated by Django 2.2 on 2019-07-07 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0006_galeria'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubNoIncluye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subnoincluye', models.CharField(max_length=100, verbose_name='Sub No Incluye')),
                ('noincluye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subnoinc', to='viajes.NoIncluye')),
            ],
        ),
        migrations.CreateModel(
            name='SubIncluye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subincluye', models.CharField(max_length=100, verbose_name='Sub Incluye')),
                ('incluye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subinc', to='viajes.Incluye')),
            ],
        ),
    ]
