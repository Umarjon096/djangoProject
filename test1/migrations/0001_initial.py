# Generated by Django 4.1.7 on 2023-03-21 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='files/')),
                ('duration', models.IntegerField(default=15)),
                ('order', models.IntegerField(default=0)),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.monitor')),
            ],
        ),
    ]