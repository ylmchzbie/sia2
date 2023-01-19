# Generated by Django 4.1.5 on 2023-01-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_aircon', '0003_technician_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='supplier_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppName', models.CharField(max_length=255)),
                ('suppAddress', models.CharField(max_length=255)),
                ('suppEmail', models.CharField(max_length=255)),
                ('suppPhone', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='tools_inventory',
            name='item_type',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]