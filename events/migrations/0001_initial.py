# Generated by Django 4.1.7 on 2023-04-12 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=200)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('event_time', models.TimeField(blank=True, null=True)),
                ('event_duration', models.CharField(blank=True, max_length=200, null=True)),
                ('event_location', models.CharField(blank=True, max_length=200, null=True)),
                ('event_description', models.TextField(blank=True, null=True)),
                ('event_attendees', models.IntegerField(default=0)),
                ('event_attendees_limit', models.IntegerField(default=0)),
                ('event_attendees_list', models.TextField(blank=True, default='', null=True)),
                ('event_winners_list', models.TextField(blank=True, default='', null=True)),
                ('fest', models.CharField(blank=True, choices=[('syntaxia', 'SYNTAXIA'), ('multiplexer', 'MULTIPLEXER'), ('gaming', 'GAMING')], default=None, max_length=15, null=True)),
                ('rules', models.TextField(blank=True, null=True)),
                ('img_url', models.CharField(blank=True, max_length=200, null=True)),
                ('prereq', models.TextField(blank=True, null=True)),
                ('team_limit', models.IntegerField(default=1)),
                ('event_head', models.CharField(blank=True, max_length=200, null=True)),
                ('event_head_contact', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_registration_date', models.DateField(auto_now_add=True, null=True)),
                ('event_registration_time', models.TimeField(auto_now_add=True, null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]