# Generated by Django 4.0 on 2022-02-26 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_vendor_customer_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='passwrd',
            new_name='password',
        ),
    ]
