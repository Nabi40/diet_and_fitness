# Generated by Django 4.1.7 on 2023-08-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_remove_data_medical_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='data1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegetables', models.CharField(max_length=1000)),
                ('weight', models.CharField(max_length=1000)),
                ('sex', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=110)),
                ('disease', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
