# Generated by Django 2.0.6 on 2018-07-30 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osm', '0001_initial'),
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='branch',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='osm.BussinessBranch'),
        ),
        migrations.AddField(
            model_name='discount',
            name='bussiness',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='osm.Bussiness'),
        ),
    ]
