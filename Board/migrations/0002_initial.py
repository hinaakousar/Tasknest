# Generated by Django 5.0.3 on 2024-03-26 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Board', '0001_initial'),
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board_m',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ticket.project_m'),
        ),
        migrations.AddField(
            model_name='label_m',
            name='board_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.board_m'),
        ),
    ]