# Generated by Django 4.2.7 on 2023-12-05 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('github', models.CharField(max_length=255)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Profile/Employee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('github', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Profile/Client')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('github', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Profile/Client/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
