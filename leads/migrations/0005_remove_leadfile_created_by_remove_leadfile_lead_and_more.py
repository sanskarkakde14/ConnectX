# Generated by Django 4.2.4 on 2023-10-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_leadfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadfile',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='leadfile',
            name='lead',
        ),
        migrations.RemoveField(
            model_name='leadfile',
            name='team',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='description',
        ),
        migrations.AddField(
            model_name='lead',
            name='Address',
            field=models.TextField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='lead',
            name='phone',
            field=models.CharField(default=' ', max_length=10),
        ),
        migrations.AddField(
            model_name='lead',
            name='property_locality',
            field=models.CharField(default=' ', max_length=25),
        ),
        migrations.AddField(
            model_name='lead',
            name='property_price',
            field=models.IntegerField(default='00'),
        ),
        migrations.AddField(
            model_name='lead',
            name='property_size',
            field=models.CharField(default=' ', max_length=25),
        ),
        migrations.AddField(
            model_name='lead',
            name='property_type',
            field=models.CharField(choices=[('plot', 'plot'), ('readyToMove', 'readyTomove'), ('apartment', 'apartment')], default='plot', max_length=11),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='LeadFile',
        ),
    ]
