from django.contrib.messages.api import get_messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Users
import hashlib
import json

# Create your views here.
def home(request) :
    try:
        if request.session['error'] == 'error':
            del request.session['error']
            return render(request, "./home.html", {'error': 'error'})
    except:
        pass
    try:
        if request.session['error2'] == 'error2':
            del request.session['error2']
            return render(request, './home.html', {'error2': 'error2'})
    except:
        pass
    return render(request, './home.html')

def timeline(request):
    try:
        id = request.session['id']
    except:
        redirect('/')
    try:
        user = Users.objects.get(hashid=id)
        if user.photo != "":
            params = {
                'name': user.name,
                'mail': user.mail,
                'photo': f'/media/{user.photo}'
            }
            return render(request, "./timeline.html", params)
        else:
            params = {
                'name': user.name,
                'mail': user.mail,
                'photo': '/media/avtar.png'
            }
            return render(request, "./timeline.html", params)
    except Exception as e:
        print(e)
        request.session['error2'] = 'error2'
        return redirect('/')

def signup(request):
    try:
        if request.session['error'] == 'error':
            del request.session['error']
            return render(request, "./signup.html", {'error': 'error'})
    except:
        return render(request, './signup.html')

def register(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    number = request.POST.get("number")
    passwd = request.POST.get("passwd")
    passwd = hashlib.md5(passwd.encode())
    passwd = passwd.hexdigest()
    hashid = hashlib.md5(email.encode())
    hashid = hashid.hexdigest()
    try:
        user = Users.objects.get(mail=email)
    except:
        adduser = Users.objects.create(name=name, mail=email, number=number, passwd=passwd, hashid=hashid)
        check = adduser.save()
        if check == None:
            return redirect("Chat Seguro")   
        else:
            return redirect("/error/")
    if user.mail == email:
        request.session['error'] = 'error'
        return redirect("/signup/")
         
        
def login(request):
    email = request.POST.get("email")
    passwd = request.POST.get("passwd")
    passwd = hashlib.md5(passwd.encode())
    passwd = passwd.hexdigest()
    try:
        user = Users.objects.get(mail=email)
    except:
        request.session['error'] = 'error'
        return redirect('/')
    if user.passwd == passwd:
        request.session['id'] = user.hashid
        return redirect("/timeline/") 
    else:
        request.session['error'] = 'error'
        return redirect('/')
    
        

def contect(request):
    return render(request, "./contect.html")

def forgotpasswd(request):
    return render(request, "./forgotpasswd.html")

def error(request):
    return render(request, "error.html")

def logout(request):
    del request.session['id']
    return redirect('/')

def get_support(request):
    pass


def searchUser(request):
    userquery = request.GET.get("q")
    q = userquery
    username = request.GET.get("user")
    try:
        usermail = Users.objects.filter(mail__icontains=q)
        userName = Users.objects.filter(name__icontains=q)
        tempdata = []
        userList = []
        for i in usermail:
            if i != username:
                if i not in tempdata:
                    tempdata.append(i)
        for i in userName:
            if i != username:
                if i not in tempdata:
                    tempdata.append(i)
        for index, email in enumerate(tempdata):
            formDB = Users.objects.get(mail=email)
            if (formDB.photo != ""):
                photo = f"/media/{formDB.photo}"
            else:
                photo = "/media/avtar.png"
            userList.append([formDB.name, formDB.mail, photo, formDB.hashid])
        return HttpResponse(userList)
    except:
        return HttpResponse("No data available")
    
def story(request):
    return HttpResponse("")
