# Generated by Django 4.1.5 on 2023-01-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oddam_w_dobre_rece', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]