# Generated by Django 2.2 on 2019-04-06 21:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20190406_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guess',
            old_name='correct_colors',
            new_name='black_pegs',
        ),
        migrations.RenameField(
            model_name='guess',
            old_name='correct_positions',
            new_name='white_pegs',
        ),
        migrations.AlterField(
            model_name='guess',
            name='code_guess',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('WHITE', 'WHITE'), ('YELLOW', 'YELLOW'), ('ORANGE', 'ORANGE'), ('RED', 'RED'), ('GREEN', 'GREEN'), ('BLUE', 'BLUE'), ('BROWN', 'BROWN'), ('BLACK', 'BLACK')], max_length=10), editable=False, size=4),
        ),
    ]
