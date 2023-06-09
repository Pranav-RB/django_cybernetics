# Generated by Django 4.1.7 on 2023-04-12 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(through='events.EventRegistration', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='eventregistration',
            unique_together={('event_id', 'user')},
        ),
    ]
