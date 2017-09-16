from django.shortcuts import render

def index(request):
    # Hub for assignment selection

    return render(request, 'grader/index.html', {})