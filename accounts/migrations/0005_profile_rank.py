# Generated by Django 4.2.4 on 2023-08-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
