from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quiz/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quiz/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=(question_id + 1))
    return render(request, 'quiz/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'quiz/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice. Numpty.",
        })
    else:
        if selected_choice.correct_choice:
                return render(request, 'quiz/correct.html', {'question': question})
        else:
                return render(request, 'quiz/incorrect.html', {'question': question})

        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('quiz:results', args=(question.id,)))

