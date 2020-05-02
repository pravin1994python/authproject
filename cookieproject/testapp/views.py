from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'testapp/name.html')

def age_view(request):
    name=request.GET['name']
    response=render(request,'testapp/age.html',{'name':name,})
    response.set_cookie('name',name)
    return response

def result_view(request):
    age=request.GET['age']
    name=request.COOKIES['name']
    response=render(request,'testapp/result.html',{'age':age,'name':name,})
    return response
