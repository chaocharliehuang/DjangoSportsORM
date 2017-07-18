from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
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

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")