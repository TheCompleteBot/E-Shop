# Generated by Django 4.0 on 2022-02-16 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.CharField(default=0, max_length=30)),
                ('description', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
