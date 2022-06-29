# Generated by Django 4.0.5 on 2022-06-29 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProbeList',
            fields=[
                ('ProbeID', models.IntegerField(primary_key=True, serialize=False)),
                ('ModelID', models.IntegerField()),
                ('Status', models.IntegerField()),
                ('CreateDate', models.DateField()),
                ('Note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProbeModelDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ModelName', models.CharField(max_length=20)),
                ('PortCount', models.IntegerField()),
                ('CPU', models.CharField(max_length=50)),
                ('Memony', models.CharField(max_length=50)),
                ('HDD', models.CharField(max_length=50)),
                ('Provider', models.IntegerField()),
                ('Note', models.CharField(max_length=200)),
            ],
        ),
    ]