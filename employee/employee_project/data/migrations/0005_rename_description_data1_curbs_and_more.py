# Generated by Django 4.1.7 on 2023-08-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_data1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data1',
            old_name='description',
            new_name='curbs',
        ),
        migrations.RenameField(
            model_name='data1',
            old_name='weight',
            new_name='fruits',
        ),
        migrations.RemoveField(
            model_name='data1',
            name='age',
        ),
        migrations.RemoveField(
            model_name='data1',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='data1',
            name='sex',
        ),
        migrations.AddField(
            model_name='data1',
            name='protein',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]