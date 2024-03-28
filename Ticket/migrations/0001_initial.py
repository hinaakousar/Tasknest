# Generated by Django 5.0.3 on 2024-03-26 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('List', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_m',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ticket_m',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('priority', models.BooleanField(default=False)),
                ('list_id', models.ManyToManyField(to='List.list_m')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user_m')),
            ],
        ),
        migrations.CreateModel(
            name='comment_m',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.ImageField(height_field=15, upload_to='', width_field=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user_m')),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ticket.ticket_m')),
            ],
        ),
    ]