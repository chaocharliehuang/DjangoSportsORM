from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from . import team_maker

def index(request):
	# Level 1

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
	}'''

	# Level 2

	''' context = {
		"teams": Team.objects.filter(league__name="Atlantic Soccer Conference")
	}

	context = {
		"players": Player.objects.filter(curr_team__location="Boston", curr_team__team_name="Penguins")
	}

	context = {
		"players": Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference')
	}

	context = {
		"players": Player.objects.filter(last_name="Lopez", curr_team__league__name='American Conference of Amateur Football')
	}

	context = {
		"players": Player.objects.filter(curr_team__league__sport='Football')
	}

	context = {
		"teams": Team.objects.filter(curr_players__first_name='Sophia')
	}

	context = {
		"leagues": League.objects.filter(teams__curr_players__first_name='Sophia')
	}

	context = {
		"players": Player.objects.filter(last_name="Flores").exclude(curr_team__location="Washington", curr_team__team_name="Roughriders")
	} '''

	# Level 3

	context = {
		"teams": Player.objects.get(first_name="Samuel", last_name="Evans").all_teams.all()
	}

	context = {
		"players": Team.objects.get(location="Manitoba", team_name="Tiger-Cats").all_players.all()
	}

	context = {
		"players": Team.objects.get(location="Wichita", team_name="Vikings").all_players.all().exclude(curr_team__location="Wichita", curr_team__team_name="Vikings")
	}

	context = {
		"teams": Player.objects.get(first_name="Jacob", last_name="Gray").all_teams.all().exclude(location="Oregon", team_name="Colts")
	}

	context = {
		"players": Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players")
	}

	context = {
		"teams": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte="12")
	}

	context = {
		"players": Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams')
	}

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")