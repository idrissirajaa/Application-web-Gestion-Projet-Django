# Generated by Django 3.2.3 on 2021-07-07 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210707_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='prenom',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
