# Generated by Django 2.1.2 on 2018-10-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_p', models.CharField(max_length=50)),
                ('apellido_m', models.CharField(max_length=50)),
                ('carnet', models.CharField(max_length=15)),
                ('tipo_seguro', models.CharField(max_length=5)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
    ]
