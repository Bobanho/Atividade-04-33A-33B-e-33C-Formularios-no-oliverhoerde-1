# Generated by Django 3.2.13 on 2023-09-06 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automotiva_bonda', '0003_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='origem',
        ),
        migrations.RemoveField(
            model_name='author',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='author',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]