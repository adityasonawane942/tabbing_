from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings


class Tournament(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tournaments")
    tournament_name = models.CharField(max_length=100)
    dates = models.CharField(max_length=100)
    speaker_score_range = models.CharField(max_length=100)
    adjudicator_score_range = models.CharField(max_length=100)
    number_of_rounds = models.CharField(max_length=100)
    number_of_break_rounds = models.CharField(max_length=100)
    tournament_venue = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('home:upload', kwargs={'pk': self.pk})

    def __str__(self):
        return self.tournament_name


class Institution(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100)
    number_of_teams = models.CharField(max_length=100)

    def __str__(self):
        return self.institution_name


class Team(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    participants_name_1 = models.CharField(max_length=100)
    participants_name_2 = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name


class Adjudicator(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    adjudicator_name = models.CharField(max_length=100)
    adjudicator_institution = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.adjudicator_name

class Venue(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    #address = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Round(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number_of_teams = models.IntegerField()
    number_of_adjudicators = models.IntegerField()
    number_of_rooms = models.IntegerField()
    number_of_adjudicators_in_a_room = models.IntegerField()
    motion = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('home:rounds', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Room(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=100)
    team1 = models.CharField(max_length=100, null=True)
    team2 = models.CharField(max_length=100, null=True)
    team3 = models.CharField(max_length=100, null=True)
    team4 = models.CharField(max_length=100, null=True)
    adjudicators = models.CharField(max_length=500)

    def __str__(self):
        return self.room_number
