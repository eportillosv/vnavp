# Generated by Django 4.0.2 on 2022-02-22 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='imagen',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nombre',
            new_name='name',
        ),
    ]
