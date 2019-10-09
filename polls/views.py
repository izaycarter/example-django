from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# list views is for many objects

# def index(request):
#     # return HttpResponse("Hello, World!")
#     question_list = Question.objects.all()
#     # output = "<br/>".join([q.question_text for q in question_list])
#     context = {
#         "question_list": question_list
#     }
#     # return HttpResponse(output)
#     return render(request, "polls/index.html", context)

class IndexView(generic.ListView):

    context_object_name = 'question_list'
    template_name = "polls/index.html"

    def get_queryset(self):
        return Question.objects.all()


# def detail(request, question_id):
#     # return HttpResponse("Details for question number %s" % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     context = {"question": question}
#     return render(request, "polls/detail.html", context)

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# def results(request, question_id):
#     # return HttpResponse("results for question number %s" % question_id)
#
#     # varibale set to object im asking fo ror 404
#     question = get_object_or_404(Question, pk=question_id)
#     # if found set value to varibel question and render
#     return render(request, "polls/results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name ="polls/results.html"

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

        # if no selected choice then error_message is prompt
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class CreateView(generic.CreateView):
    model = Question
    # fields = '__all__'
    fields = ["question_text",]
    template_name = "polls/create.html"
