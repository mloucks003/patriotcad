# Generated by Django 3.1.5 on 2024-11-15 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patriot_cadapp', '0003_auto_20210130_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='notes',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
    ]