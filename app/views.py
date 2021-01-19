from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    return HttpResponse("Hello, world. You're at the app index enter id in url for other action.")

def qna(request, ques_id):
    ques = Question.objects.get(id=ques_id)
    # arr = list()
    # for q in ques:
    #     arr.append(q.choice_set.all())
    # return HttpResponse(arr)
    response = list()
    for ch in ques.choice_set.all():
        # import pdb
        # pdb.set_trace()
        response.append(ch)
    return HttpResponse(response)