# Generated by Django 2.1.3 on 2018-11-30 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0010_auto_20181130_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='rental',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.CarRental'),
        ),
    ]
