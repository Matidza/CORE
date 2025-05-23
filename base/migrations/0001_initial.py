# Generated by Django 5.1.4 on 2025-01-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('telephone', models.CharField(blank=True, max_length=200)),
                ('schoolemail', models.EmailField(blank=True, max_length=254)),
                ('schooladdress', models.TextField(default='', max_length=100)),
                ('postal_address', models.CharField(blank=True, max_length=100)),
                ('website', models.TextField(max_length=100)),
                ('slogan', models.CharField(blank=True, max_length=200)),
                ('emblem', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/schoolprofile/')),
                ('type_of_school', models.CharField(blank=True, choices=[('Primary', 'Primary School'), ('Secondary', 'Secondary School'), ('Combined', 'Combined School'), ('Vocational', 'Vocational School'), ('Other', 'Other School')], max_length=200)),
            ],
            options={
                'verbose_name_plural': 'school profile',
            },
        ),
    ]
