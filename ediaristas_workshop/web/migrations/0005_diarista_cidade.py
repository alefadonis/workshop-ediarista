# Generated by Django 3.2.4 on 2021-06-16 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_remove_diarista_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarista',
            name='cidade',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
