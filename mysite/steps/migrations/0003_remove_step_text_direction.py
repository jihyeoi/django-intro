# Generated by Django 5.0.4 on 2024-05-01 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0002_step_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='text',
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction_text', models.TextField(default='')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='steps.step')),
            ],
        ),
    ]
