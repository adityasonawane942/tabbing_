# Generated by Django 2.2.1 on 2019-06-18 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_name', models.CharField(max_length=100)),
                ('dates', models.CharField(max_length=100)),
                ('speaker_score_range', models.CharField(max_length=100)),
                ('adjudicator_score_range', models.CharField(max_length=100)),
                ('number_of_rounds', models.CharField(max_length=100)),
                ('number_of_break_rounds', models.CharField(max_length=100)),
                ('tournament_venue', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournaments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tournament', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('participants_name_1', models.CharField(max_length=100)),
                ('participants_name_2', models.CharField(max_length=100)),
                ('institution_name', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number_of_teams', models.IntegerField(default=0)),
                ('number_of_rooms', models.IntegerField(default=0)),
                ('number_of_judges_in_a_room', models.IntegerField(default=0)),
                ('motion', models.CharField(max_length=100)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=100)),
                ('number_of_teams', models.CharField(max_length=100)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Adjudicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adjudicator_name', models.CharField(max_length=100)),
                ('adjudicator_institution', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tournament')),
            ],
        ),
    ]
