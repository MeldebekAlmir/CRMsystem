# Generated by Django 5.0.3 on 2024-04-26 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_alter_guestprofile_document_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='time_create',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time_update',
        ),
    ]
