# Generated by Django 4.0.6 on 2022-08-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeslider',
            name='long_title',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='homeslider',
            name='short_title',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
