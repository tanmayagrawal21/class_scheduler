from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models  import Teacher, Time, Day

# Create your views here.
def index(request):
    return render(request, "teachers/index.html",{
        "teachers":Teacher.objects.all(),
    })