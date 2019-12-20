from django.shortcuts import render
from chat.models.lobbies import Lobby
from django.template import loader
from django.http import HttpResponse

def base_viewer(request,context):
    return render(request, "Lobby/lobby_lists.html", context=context)