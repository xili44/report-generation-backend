# Generated by Django 5.0.7 on 2024-07-23 06:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CYP1A2', models.BooleanField()),
                ('CYP2C19', models.BooleanField()),
                ('CYP2C9', models.BooleanField()),
                ('CYP2D6', models.BooleanField()),
                ('CYP3A4', models.BooleanField()),
                ('CYP3A5', models.BooleanField()),
                ('OPRM1', models.BooleanField()),
                ('SLCO1B1', models.BooleanField()),
                ('VKORC1', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('dateOfOrder', models.DateField()),
                ('dateOfReport', models.DateField()),
                ('ethnicity', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('hn', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='HN must contains 10 numbers exactly', regex='^[0-9]{10}$')])),
                ('name', models.CharField(max_length=50)),
                ('orderedBy', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacogenomics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('drug', models.CharField(max_length=50)),
                ('gene', models.CharField(max_length=10)),
            ],
        ),
    ]
