# Generated by Django 4.2.4 on 2023-09-12 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
