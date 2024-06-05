# Generated by Django 4.2.4 on 2023-10-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_clientfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='client',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='team',
        ),
        migrations.RemoveField(
            model_name='client',
            name='description',
        ),
        migrations.AddField(
            model_name='client',
            name='Address',
            field=models.TextField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default=' ', max_length=10),
        ),
        migrations.AddField(
            model_name='client',
            name='property_locality',
            field=models.CharField(default=' ', max_length=25),
        ),
        migrations.AddField(
            model_name='client',
            name='property_price',
            field=models.IntegerField(default='00'),
        ),
        migrations.AddField(
            model_name='client',
            name='property_size',
            field=models.CharField(default=' ', max_length=25),
        ),
        migrations.AddField(
            model_name='client',
            name='property_type',
            field=models.CharField(choices=[('plot', 'plot'), ('readyToMove', 'readyTomove'), ('apartment', 'apartment')], default='plot', max_length=11),
        ),
        migrations.DeleteModel(
            name='ClientFile',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]