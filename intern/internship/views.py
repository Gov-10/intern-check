from django.shortcuts import render

# Create your views here.
def intern(request):
    return render(request, 'intern.html')
