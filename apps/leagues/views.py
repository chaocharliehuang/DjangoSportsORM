from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	''' context = {
		"leagues": League.objects.filter(sport="Baseball")
	}

	context = {
		"leagues": League.objects.filter(name__contains="Women")
	}

	context = {
		"leagues": League.objects.filter(sport__contains="Hockey")
	}

	context = {
		"leagues": League.objects.exclude(sport="Football")
	}

	context = {
		"leagues": League.objects.filter(name__contains="Conference")
	}

	context = {
		"leagues": League.objects.filter(name__contains="Atlantic")
	}

	context = {
		"teams": Team.objects.filter(location="Dallas")
	}

	context = {
		"teams": Team.objects.filter(team_name="Raptors")
	}

	context = {
		"teams": Team.objects.filter(location__contains="City")
	}

	context = {
		"teams": Team.objects.filter(team_name__startswith="T")
	}

	context = {
		"teams": Team.objects.order_by("location")
	}

	context = {
		"teams": Team.objects.order_by("-location")
	}

	context = {
		"teams": Team.objects.order_by("-location")
	}

	context = {
		"players": Player.objects.filter(last_name="Cooper")
	}

	context = {
		"players": Player.objects.filter(first_name="Joshua")
	}

	context = {
		"players": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")
	}

	context = {
		"teams": League.objects.get(name="Atlantic Soccer Conference").teams.all()
	}

	context = {
		"players": Team.objects.get(team_name="Penguins", location="Boston").curr_players.all()
	}

	context = {"players": []}
	teams = League.objects.get(name="International Collegiate Baseball Conference").teams.all()
	for team in teams:
		team_players = team.curr_players.all()
		for player in team_players:
			context['players'].append(player)
	
	context = {"players": []}
	teams = League.objects.get(name="American Conference of Amateur Football").teams.all()
	for team in teams:
		team_players = team.curr_players.all().filter(last_name="Lopez")
		for player in team_players:
			context['players'].append(player)
	
	context = {"players": []}
	leagues = League.objects.filter(sport="Football")
	for league in leagues:
		teams = league.teams.all()
		for team in teams:
			team_players = team.curr_players.all()
			for player in team_players:
				context['players'].append(player)
	
	context = {"teams": []}
	teams = Team.objects.all()
	for team in teams:
		players = team.curr_players.all()
		for player in players:
			if player.first_name == "Sophia":
				context['teams'].append(team)
				break
	
	context = {"leagues": []}
	player_found = False
	leagues = League.objects.all()
	for league in leagues:
		player_found = False
		teams = league.teams.all()
		for team in teams:
			if player_found == True:
				break
			players = team.curr_players.all()
			for player in players:
				if player.first_name == "Sophia":
					context['leagues'].append(league)
					player_found = True
					break '''
	
	context = {"players": []}
	players = Player.objects.filter(last_name="Flores")
	for player in players:
		if player.curr_team.team_name != "Roughriders" and player.curr_team.location != "Washington":
			context['players'].append(player)


	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")