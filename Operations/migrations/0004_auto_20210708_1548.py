# Generated by Django 3.2.3 on 2021-07-08 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Operations', '0003_auto_20210708_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tache',
            old_name='date_debut',
            new_name='debut',
        ),
        migrations.RenameField(
            model_name='tache',
            old_name='date_fin',
            new_name='fin',
        ),
    ]