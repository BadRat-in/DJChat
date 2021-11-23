from django.contrib.messages.api import get_messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Users, Message
import hashlib
import json, requests as https, random
from datetime import datetime
from django.db.models import Q

# Create your views here.
def home(request) :
    isMobile = request.user_agent.is_mobile
    isTab = request.user_agent.is_tablet
    if (isTab or isMobile):
        return render(request, "./formobileortab.html")
    else:
        try:
            id = request.session['id']
            return redirect('/timeline/')
        except:
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
                'photo': f'/media/{user.photo}',
                'id': user.hashid,
            }
            return render(request, "./timeline.html", params)
        else:
            params = {
                'name': user.name,
                'mail': user.mail,
                'photo': '/media/avtar.png',
                'id': user.hashid,
            }
            return render(request, "./timeline.html", params)
    except Exception as e:
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
        adduser = Users.objects.create(name=name, mail=email, number=number, passwd=passwd, hashid=hashid, status=0)
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
        user.status = 1
        user.save()
        return redirect("/timeline/") 
    else:
        request.session['error'] = 'error'
        return redirect('/')
    
        

def contect(request):
    return render(request, "./contect.html")

def forgotpasswd(request):
    return render(request, "./forgotpasswd.html")

def error(request, *args, **kwargs):
    return render(request, "error.html")

def logout(request):
    id = request.session['id']
    user = Users.objects.get(hashid=id)
    user.status = 0
    user.save()
    Users.objects.update(status=0)
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
        usertemp = []
        for i in tempdata:
            if str(i) != username:
                usertemp.append(i)
        for index, email in enumerate(usertemp):
            formDB = Users.objects.get(mail=email)
            if (formDB.photo != ""):
                photo = f"../media/{formDB.photo}"
            else:
                photo = "../media/avtar.png"
            userList.append([formDB.name, formDB.mail, photo, formDB.hashid, formDB.status, formDB.number])
        return HttpResponse(userList)
    except:
        return HttpResponse("No data available")
    
    
def getUser(request):
    reciever = request.GET.get("me")
    try:
        msg = Message.objects.filter(reciever=reciever)
        hashtemp = []
        userhashtemp = []
        userList = []
        for i in msg:
            hashtemp.append(i)
        hashtemp = list(dict.fromkeys(hashtemp))
        for hashid in hashtemp:
            user = Message.objects.get(hashid=hashid)
            userhashtemp.append(user.sender)
        userhashtemp = list(dict.fromkeys(userhashtemp))
        msg = Message.objects.filter(sender=reciever)
        for i in msg:
            hashtemp.append(i)
        hashtemp = list(dict.fromkeys(hashtemp))
        for hashid in hashtemp:
            user = Message.objects.get(hashid=hashid)
            userhashtemp.append(user.reciever)
        userhashtemp = list(dict.fromkeys(userhashtemp))
        userhashtemp2 = []
        for i in userhashtemp:
            if i != reciever:
                userhashtemp2.append(i)
        for hashid in userhashtemp2:
            formDB = Users.objects.get(hashid=hashid)
            if (formDB.photo != ""):
                photo = f"../media/{formDB.photo}"
            else:
                photo = "../media/avtar.png"
            userList.append([formDB.name, formDB.mail, photo, formDB.hashid, formDB.status, formDB.number])
            
        return HttpResponse(userList)    
    except:
        return HttpResponse("")
    
def story(request):
    return HttpResponse("")


def matchnumber(request):
    num = request.GET.get("num")
    mail = request.GET.get("mail")
    try:
        from_db = Users.objects.get(number=num)
        if (from_db.number == num and from_db.mail == mail):
            otp = ""
            for i in range(7):
                otp = otp + str(random.randrange(9))
            msg = f"Chat Seguro:\nOTP for password reset : {otp}. Do't share with anyone."
            url = f"https://www.fast2sms.com/dev/bulkV2?authorization=2Gj5CQ7ZplKO6dBPLr3Xu8qVtIaesvJoTfHzRcDb0MknhUYFASWixSuo9czmYydTjUD2VXRsHwMlhQGv&route=v3&sender_id=TXTIND&message={msg}&language=english&flash=0&numbers={num}"
            otp_response = https.get(url)
            if(str(otp_response) == "<Response [200]>"):
                obj = [hashlib.md5(otp.encode()).hexdigest(),"\n", from_db.hashid]
                return HttpResponse(obj)
            else:
                return HttpResponse("failed")
        else:
            return HttpResponse("not-match")
    except:
        return HttpResponse("not-match")
    
def resetpass(request):
    hashid = request.GET.get("hashid")
    return render(request, "resetpass.html", {"hashid": hashid})

def savepass(request):
    hashid = request.GET.get("hashid")
    passwd = request.GET.get("passwd")
    passwd = hashlib.md5(passwd.encode())
    passwd = passwd.hexdigest()
    user = Users.objects.get(hashid=hashid)
    user.passwd = passwd
    user.save()
    return HttpResponse("Done")

def sendStatus(request):
    id = request.GET.get('q')
    user = Users.objects.get(hashid=id)
    return HttpResponse(user.status)


def saveMessage(request):
    Time = datetime.now()
    ms = ""
    for i in range(10):
        ms = ms + str(random.randrange(9))
    temp = Time.strftime("%Y%m%d%H%M%S")
    temp = temp + ms
    msg = request.GET.get("msg")
    sender = request.GET.get("me")
    reciever = request.GET.get("you")
    time = request.GET.get("time")
    temp_msg = Message.objects.create(message=msg, sender=sender, reciever=reciever, time=time, date=Time.strftime("%Y-%m-%d"), hashid=hashlib.md5(temp.encode()).hexdigest())
    check = temp_msg.save()
    if check != None:
        return HttpResponse("Send")
    else:
        return HttpResponse("fail")


def getMessage(request):
    reciever = request.GET.get("me")
    sender = request.GET.get("you")
    try:
        hashtemp = Message.objects.filter(Q(reciever=reciever) | Q(reciever=sender), Q(sender=sender) | Q(sender=reciever))
        msgtemp = []
        for i in hashtemp:
                msg = Message.objects.get(hashid=i)
                msg.isDeliver = 1
                msg.save()
                msgtemp.append([msg.hashid, msg.message, msg.sender, str(msg.time), str(msg.date)])
        return HttpResponse(msgtemp)
    except:
        return HttpResponse("")
    
def cmsg(request):
    reciever = request.GET.get("me")
    sender = request.GET.get("you")
    try:
        hashtemp = Message.objects.filter(reciever=reciever, sender=sender)
        msgtemp = []
        for i in hashtemp:
                msg = Message.objects.get(hashid=i)
                if msg.isDeliver != 1:
                    msg.isDeliver = 1
                    msg.save()
                    msgtemp.append([msg.hashid, msg.message, msg.sender, str(msg.time), str(msg.date)])
        return HttpResponse(msgtemp)
    except:
        return HttpResponse("")
    
    