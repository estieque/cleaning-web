# Generated by Django 4.0.6 on 2022-08-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='meta_description',
            field=models.CharField(max_length=155),
        ),
    ]
