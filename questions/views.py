from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from questions.models import SolveForm, Question, Comment
from users.models import Profile


from questions.forms import QuestionForm
from django.utils.dateparse import parse_duration


@login_required
def list_questions(request):
    questions = Question.objects.all().order_by('-post_date')
    return render(
        request=request,
        template_name='questions/q_feed.html',
        context={
            'questions':questions,
            'user':request.user
            }
        )

@login_required
def new_question(request):
    ''' Add a new question '''

    if request.method == 'POST':

        form_data = request.POST.copy()
        form_data['author'] = Profile.objects.get(id=request.user.profile.id)

        # import ipdb
        # ipdb.set_trace()
        time_to_solve = parse_duration(form_data['time_to_solve'])

        question = Question.objects.create(
            author=form_data['author'],
            time_to_solve = time_to_solve,
            description = form_data['description'],
            technology_tag = form_data['technology'],
        )

        # if form.is_valid():
        return redirect('q_feed')

    else:
        form = QuestionForm()

    return render(request,'questions/new_question.html', context={'form':form,'user':request.user})


@login_required
def question_detail(request, id):
    # import ipdb ; ipdb.set_trace()
    question = Question.objects.get(id=id)
    comments = Comment.objects.all().filter(question = id)

    if request.method == 'POST':
        author = Profile.objects.get(id=request.user.profile.id)
        content = request.POST['content']

        comment = Comment.objects.create(
            author=author,
            question=question,
            content = content,
        )

        return redirect('question_detail', id=id)

    return render(request,'questions/question_detail.html',{'question':question, 'comments':comments})