from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from questions.models import Technologie, SolveForm, Question, Comment


@login_required
def list_questions(request):
    return render(request, 'questions/q_feed.html')