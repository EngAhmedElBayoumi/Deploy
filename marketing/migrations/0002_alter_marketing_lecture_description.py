# Generated by Django 4.2.4 on 2023-08-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketing_lecture',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
