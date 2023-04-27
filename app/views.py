from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    d={'TFO':TopicForm()}
    if request.method=='POST':
        TOF=TopicForm(request.POST)
        if TOF.is_valid():
            TOF.save()
            return HttpResponse('<h1>The data is inserted </h1>')
        else:
            return HttpResponse('<h1>The data is not valid</h1>')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    d={'WFO':WebpageForm()}
    if request.method=='POST':
        WO=WebpageForm(request.POST)
        if WO.is_valid():
            WO.save()
            return HttpResponse('<h1> data is inserted</h1>')
        else:
            return HttpResponse(f'<h1> data is not valid</h1>')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    d={'AFO':AccessRecordForm()}
    if request.method=='POST':
        AO=AccessRecordForm(request.POST)
        if AO.is_valid():
            AO.save()
            return HttpResponse('<h1>The data is inserted</h1>')
        else:
            return HttpResponse('<h1>The data is not valid</h1>')
    return render(request,'insert_access.html',d)