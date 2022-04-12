from django.contrib import admin
from ipl_app.models import Team,Player

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display=['team_name','team_icon','team_player_count','team_top_bat',
	'team_top_bowl','team_won_count']
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	list_display=['player_name','player_photo','player_team','player_price',
	'player_play_status','team_role']
