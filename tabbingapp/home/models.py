from django.db import models
from django.urls import reverse


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=100)
    dates = models.CharField(max_length=100)
    speaker_score_range = models.CharField(max_length=100)
    adjudicator_score_range = models.CharField(max_length=100)
    number_of_rounds = models.CharField(max_length=100)
    number_of_break_rounds = models.CharField(max_length=100)
    tournament_venue = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('home:homepage', kwargs={'pk': self.pk})

    def __str__(self):
        return self.tournament_name


class Institution(models.Model):
    institution_name = models.CharField(max_length=100)
    number_of_teams = models.CharField(max_length=100)

    def __str__(self):
        return self.institution_name


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    participants_name = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class Adjudicator(models.Model):
    adjudicator_name = models.CharField(max_length=100)
    adjudicator_institution = models.CharField(max_length=100)

    def __str__(self):
        return self.adjudicator_name
