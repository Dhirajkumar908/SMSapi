from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    user=request.GET.get('user')
    password=request.GET.get('Password') 
    url=f"http://nimbusit.biz/api/SmsApi/CheckBalance?UserID={user}&Password={password}"
    response=requests.get(url)
    data=response.json()
    # Response=data[Response]
    print(data)
    context={
        'data':data,
    }
    return render(request, 'balance.html', context)

#UserID=testdemo&Password=cbhe1755CB
def sendSMS(request):
    user=request.GET.get('user')
    password=request.GET.get('Password')
    SenderID=request.GET.get('SenderID')
    Phno=request.GET.get('Phno')
    Msg=request.GET.get('Msg')
    EntityID=request.GET.get('EntityID')
    TemplateID=request.GET.get('TemplateID')
    urls=f"http://nimbusit.biz/api/SmsApi/SendSingleApi?UserID={user}&Password={password}&SenderID={SenderID}&Phno={Phno}&Msg={Msg}&EntityID={EntityID}&TemplateID={TemplateID}"
    response=requests.get(urls)
    datas=response.json()
    context={
        'datas':datas,
        'urls':urls
    }
    return render(request, 'balance.html', context)

def info(request):
    return render(request, 'info.html')