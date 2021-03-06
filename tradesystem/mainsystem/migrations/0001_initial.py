# Generated by Django 3.2.9 on 2021-12-07 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('broker_name', models.CharField(max_length=50)),
                ('broker_username', models.CharField(max_length=50)),
                ('broker_password', models.CharField(max_length=500)),
                ('broker_api', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('broker_username', models.CharField(max_length=20)),
                ('orderId', models.IntegerField()),
                ('variety', models.CharField(max_length=20)),
                ('tradingsymbol', models.CharField(max_length=50)),
                ('transactiontype', models.CharField(max_length=10)),
                ('exchange', models.CharField(max_length=10)),
                ('ordertype', models.CharField(max_length=30)),
                ('producttype', models.CharField(max_length=20)),
                ('duration', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('timedate', models.DateTimeField()),
            ],
        ),
    ]
