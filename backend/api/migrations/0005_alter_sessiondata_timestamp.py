# Generated by Django 5.1.1 on 2024-10-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_session_session_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiondata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
