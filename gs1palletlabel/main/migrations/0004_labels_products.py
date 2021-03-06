# Generated by Django 4.0 on 2022-01-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_destinations_options_alter_suppliers_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=25, verbose_name='OrderNumber')),
                ('supplier_id', models.SmallIntegerField(verbose_name='SupplierID')),
                ('destination_id', models.SmallIntegerField(verbose_name='DestinationID')),
                ('pallets_count', models.SmallIntegerField(verbose_name='PalletsCount')),
                ('product_id', models.SmallIntegerField(verbose_name='ProductID')),
                ('link_to_pdf', models.CharField(max_length=500, verbose_name='LinkToPdf')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, verbose_name='ProductName')),
                ('product_scu', models.CharField(max_length=16, verbose_name='ProductSCU')),
                ('boxes_per_pallet', models.SmallIntegerField(verbose_name='BoxesPerPallet')),
                ('weight_brutto', models.CharField(max_length=8, verbose_name='WeightBrutto')),
                ('weight_netto', models.CharField(max_length=8, verbose_name='WeightNetto')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
