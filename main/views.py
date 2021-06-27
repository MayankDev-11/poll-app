from main.models import Question
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
    questions = Question.objects.order_by('-pub_date')
    paginator = Paginator(questions,8)
    page = request.GET.get('page')
    paged_questions = paginator.get_page(page)
    data = {
        'questions':paged_questions,
        # 'page':paged_questions,
    }
    return render(request, 'pages/home.html', data)


def create_poll(request):
    if request.method == 'POST':
        app = Question()
        question = request.POST.get('question',False)
        option_1 = request.POST.get('Option-1',False)
        option_2 = request.POST.get('Option-2',False)
        option_3 = request.POST.get('Option-3',False)
        option_4 = request.POST.get('Option-4',False)

        if len(request.FILES) != 0:
            image = request.FILES['image']
        
        poll = Question(question=question,option_1=option_1, option_2=option_2, option_3=option_3, option_4=option_4, image=image)
        poll.save()
        return redirect('/')

    return render(request, 'pages/create_poll.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    question = Question.objects.filter(pk=question_id)
    data = {
        'question':question,
    }

    return render(request, 'pages/results.html', data)

def vote(request, question_id):
    question = Question.objects.filter(pk=question_id)
    poll = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        print(Question.optionone_count)
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.optionone_count += 1
        elif selected_option == 'option2':
            poll.optiontwo_count += 1
        elif selected_option == 'option3':
            poll.optionthree_count += 1
        elif selected_option == 'option4':
            poll.optionfour_count += 1
        else:
            return HttpResponse(400,'Invalid Form')        
        poll.save()

        return redirect('results', poll.id)

    data = {
        'question':question,
    }
    return render(request,'pages/vote.html', data)
