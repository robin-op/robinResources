# Generated by Django 2.2.6 on 2019-11-11 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('profesor', 'Es profesor'), ('alumno', 'Es alumno'))},
        ),
    ]