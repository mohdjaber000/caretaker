# Generated by Django 2.0 on 2018-02-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0002_auto_20180216_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='cashdecrement',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='cashincrement',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
