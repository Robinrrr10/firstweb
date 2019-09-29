from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Helloworld!")

def profile(request):
    mypage = "<h1>hello</h1><h2>boss</h2>"
    return HttpResponse(mypage)

def home2(request):
    return render(request, 'myhome2page.html')

def home3(request):
    mname = "Rahul"
    return render(request, 'myhome3page.html', {'name':mname})

def home4(request):
    return render(request, 'mpage5.html')

def addPage(request):
    return render(request, 'addition.html')

def performAddition(request):
    var1 = int(request.GET["num1"])
    var2 = int(request.GET["num2"])
    res = var1 + var2
    return render(request, 'result.html', {'addresult':res})

def signPage(request):
    return render(request, 'signp.html')

def dosign(request):
    print("comming here")
    email = request.POST['email']
    passd = request.POST['password']
    signresult = "Not successfull"
    if email == "hi123@gmail.com" and passd == "12345":
        signresult = "Successfull"
    print("result is:", signresult)
    return render(request, 'signresult.html', {'signrest': signresult})


