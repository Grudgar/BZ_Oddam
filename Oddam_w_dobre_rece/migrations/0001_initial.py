# Generated by Django 4.1.5 on 2023-01-18 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[(1, 'Fundacja'), (2, 'Organizacja pozarządowa'), (3, 'Zbiórka lokalna')], default=1, max_length=64)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Oddam_w_dobre_rece.category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=64)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.IntegerField()),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Oddam_w_dobre_rece.category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Oddam_w_dobre_rece.institution')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
