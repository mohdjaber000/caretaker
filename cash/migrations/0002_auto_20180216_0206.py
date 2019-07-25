# Generated by Django 2.0 on 2018-02-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash',
            name='balance',
            field=models.DecimalField(decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='cash',
            name='currency',
            field=models.CharField(blank=True, default='GHC', max_length=64),
        ),
    ]
