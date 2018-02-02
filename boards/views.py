from django.shortcuts import render
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = Board.objects.get(pk=pk)  # recupera o board da DB com o a PK
    return render(request, 'topics.html', {'board': board})
