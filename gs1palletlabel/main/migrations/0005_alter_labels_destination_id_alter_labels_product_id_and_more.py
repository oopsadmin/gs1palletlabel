# Generated by Django 4.0 on 2022-01-03 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_labels_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labels',
            name='destination_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.destinations'),
        ),
        migrations.AlterField(
            model_name='labels',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.products'),
        ),
        migrations.AlterField(
            model_name='labels',
            name='supplier_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.suppliers'),
        ),
    ]
