# Generated by Django 5.1.1 on 2024-10-05 04:37

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_start', models.DateTimeField(auto_now_add=True)),
                ('time_end', models.DateTimeField(null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SessionData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('pressure_1', models.FloatField()),
                ('pressure_2', models.FloatField()),
                ('pressure_3', models.FloatField()),
                ('pressure_4', models.FloatField()),
                ('accel_x', models.FloatField()),
                ('accel_y', models.FloatField()),
                ('accel_z', models.FloatField()),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_data', to='api.session')),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
