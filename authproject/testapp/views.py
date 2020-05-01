from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage_view(request):
    return render(request,'testapp/home.html')

@login_required
def javapage_view(request):
    return render(request,'testapp/java.html')
