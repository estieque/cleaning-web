# Generated by Django 4.0.6 on 2022-08-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSub',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]