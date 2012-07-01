from django.shortcuts import render

def view(request):
    return render(request, 'unfiled/view.html')
