# Generated by Django 4.0.5 on 2022-07-02 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TIPO_PRODUCTO',
            fields=[
                ('id_tipo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tipo_producto',
            },
        ),
        migrations.CreateModel(
            name='PRODUCTO',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='productos')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipo_producto')),
            ],
            options={
                'db_table': 'producto',
            },
        ),
    ]
