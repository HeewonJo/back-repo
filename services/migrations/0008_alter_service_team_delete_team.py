# Generated by Django 5.1.2 on 2024-11-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_team_alter_service_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='team',
            field=models.IntegerField(unique=True),
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]