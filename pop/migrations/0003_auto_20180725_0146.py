# Generated by Django 2.0.6 on 2018-07-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0002_auto_20180220_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashpurchase',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cashpurchasereturn',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='creditpurchase',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='creditpurchasereturn',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
