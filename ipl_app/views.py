from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from ipl_app.models import Team, Player
from django.contrib import messages
from ipl_app.forms import teamform,playerform
from django.core import serializers
import json
import string
import random
# Create your views here.

def getRandomString(stringLength=10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def teamdisplay(request):
	team_data=Team.objects.all()
	return render(request, "index.html", {"Team":team_data})

def search(request):
	query=request.GET['query']
	#search=Team.objects.all()
	if query:
		search=Team.objects.filter(team_name__icontains=query)
		srch_rslt={"search":search}
		return render(request,"team_search.html", srch_rslt)
	else:
		messages.success(request,"No Search Result...!")
		return render(request,"team_search.html",)

	#return HttpResponse('This is search')

def teamInsert(request):
	if request.method=="POST":
		if request.POST.get('team_name') or request.POST.get('team_icon') or request.POST.get('team_player_count') or request.POST.get('team_top_bat') or request.POST.get('team_top_bowl') or request.POST.get('team_won_count'):
			saveteam=Team()
			saveteam.team_name=request.POST.get('team_name')
			saveteam.team_name=request.POST.get('team_name')
			saveteam.team_icon=request.FILES['team_icon']
			saveteam.team_player_count=request.POST.get('team_player_count')
			saveteam.team_top_bat=request.POST.get('team_top_bat')
			saveteam.team_top_bowl=request.POST.get('team_top_bowl')
			saveteam.team_won_count=request.POST.get('team_won_count')
			saveteam.save()
			messages.success(request,"The team "+saveteam.team_name+" is added successfully...!")
			return render(request,"team_create.html")
		else:
			messages.success(request,"Fill Out the Team Details...!")
			return render(request,"team_create.html")
	return render(request,"team_create.html")



def teamedit(request,id):
	getteamdetails=Team.objects.get(id=id)
	return render(request,"edit.html",{"Team":getteamdetails})

def teamupdate(request,id):
	teamupdate=Team.objects.get(id=id)
	form=teamform(request.POST,instance=teamupdate)
	if form.is_valid():
		form.save()
		messages.success(request,"Update successfully...!")
		return render(request,"edit.html",{"Team":teamupdate})

def teamdel(request,id):
	delteam=Team.objects.get(id=id)
	delteam.delete()
	return HttpResponseRedirect('/')
	#team_data=Team.objects.all()
	#return render(request, "index.html",{"Team":team_data})

def teamdetails(request,id):
	teamdetails=Team.objects.get(id=id)
	print("teamdetails",request)
	query_set=Team.objects.filter(id=id)
	query_set=serializers.serialize('json',query_set)
	Team_icon=json.loads(query_set)
	print(Team_icon[0]['fields']['team_icon'])
	Team_icon='http://localhost:8000/'+Team_icon[0]['fields']['team_icon']
	print(Team_icon)
	allplayers=Player.objects.filter(player_team=id)
	return render(request,"team_details.html",{"Team":teamdetails,"allplayers":allplayers,"team_icon":Team_icon})

def add_player(request):
	if request.method=="POST":
		if request.POST.get('player_name') or request.POST.get('player_photo') or request.POST.get('player_team') or request.POST.get('player_price') or request.POST.get('player_play_status') or request.POST.get('team_role'):
			saveplayer=Player()
			print(request.POST.get('player_team'))
			query_set=Team.objects.filter(team_name=request.POST.get('player_team'))
			query_set=serializers.serialize('json',query_set)
			team_id=json.loads(query_set)
			team_id=team_id[0]['pk']
			saveplayer.player_name=request.POST.get('player_name')
			saveplayer.player_photo=request.FILES['player_photo']
			saveplayer.player_team=team_id
			saveplayer.player_price=request.POST.get('player_price')
			saveplayer.player_play_status=request.POST.get('player_play_status')
			saveplayer.team_role=request.POST.get('team_role')
			saveplayer.save()
			messages.success(request,"The Player "+saveplayer.player_name+" is added successfully...!")
			return render(request,"player_create.html")
		else:
			messages.success(request,"Fill Out Player Details...!")
			return render(request,"player_create.html")
	else:
		Team_name=Team.objects.values('team_name').order_by('id')
		print(Team_name)
		t_list=[]
		for course in Team_name:
			print(course['team_name'])
			t_list.append(course['team_name'])
		context={'team_list':t_list}
		return render(request,"player_create.html",context)

def playerdetails(request,id):
	playerdetails=Player.objects.get(id=id)
	query_set=Player.objects.filter(id=id)
	query_set=serializers.serialize('json',query_set)
	p_icons=json.loads(query_set)
	# print(p_icon)
	player_icon='http://localhost:8000/'+p_icons[0]['fields']['player_photo']
	print(player_icon)
	# id=p_icon[0]['fields']['p_team']
	query_set=Team.objects.filter(id=int(p_icons[0]['fields']['player_team']))
	query_set=serializers.serialize('json',query_set)
	teamdata=json.loads(query_set)
	print(teamdata)
	team_name=teamdata[0]['fields']['team_name']

	return render(request, "player_profile.html", {"Player":playerdetails,"player_icon":player_icon,"team_name":team_name})
