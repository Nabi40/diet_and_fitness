# Generated by Django 4.1.7 on 2023-08-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.CharField(max_length=1000)),
                ('lunch', models.CharField(max_length=1000)),
                ('snacks', models.CharField(max_length=1000)),
                ('dinner', models.CharField(max_length=1000)),
                ('Notes', models.CharField(max_length=1000)),
            ],
        ),
    ]
