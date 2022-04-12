from django.db import models

# Create your models here.
class Team(models.Model):
	team_name = models.CharField(max_length=100, null=True, blank=True)
	team_icon = models.FileField(upload_to='media/ticon/', null=True)
	team_player_count = models.IntegerField(null=True, blank=True)
	team_top_bat = models.CharField(max_length=500, null=True, blank=True)
	team_top_bowl = models.CharField(max_length=500, null=True, blank=True)
	team_won_count = models.IntegerField(null=True, blank=True)
class Player(models.Model):
	player_name = models.CharField(max_length=100, null=True, blank=True)
	player_photo = models.FileField(upload_to='media/photo/', null=True)
	player_team = models.CharField(max_length=500, null=True, blank=True)
	player_price = models.CharField(max_length=500, null=True, blank=True)
	player_play_status = models.CharField(max_length=500, null=True, blank=True)
	team_role = models.CharField(max_length=500, null=True, blank=True)