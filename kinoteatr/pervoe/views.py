from django.shortcuts import render
import datetime
import random
from .models import Post
from .models import Film
from .models import LK
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.utils.translation import ugettext as _
from django.shortcuts import redirect

class form1(forms.Form):
    name = forms.CharField(label=_(u'Заголовок'), max_length=20)
    
class form2(forms.Form):
    age = forms.CharField(label=_(u'Текст поста'), max_length=2000)


def log(request):
    
    user = ""
    password = ""
    err = ""
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
    user_a = authenticate(username=user, password=password)
    if user_a is not None:
        login(request, user_a)
        context = {"Пользователь авторизован" + user}
        return redirect("/film")
    else:
        context = {'error': err}
        return render(request, "log.html", context)

def logout1(request):
    logout(request)
    return redirect("/film")
    



def create(request):   
    if request.method == "POST":
        bd = Post()
        bd.title = request.POST.get("name")
        bd.text = request.POST.get("age")
        bd.save()
    people = Post.objects.all()
    #people.delete()
    i = 0
    form01 = form1(request.POST or None )
    form02 = form2(request.POST or None )
    context = { 'formZ': form01,'formP': form02, 'people': people, 'i': i }
    
    return render(request, "create.html", context )

def index(request):
    #logout(request)
    #post1 = Post.objects.all()
    #user = User.objects.create_user('pasha', 'lennon@thebeatles.com', '123456')
    ##user.last_name = 'Lennon'
    #user.save()
    #return render(request, "index.html", {"post1": post1})
    return redirect("/film")

def lk(request):
    if request.user.is_authenticated:
        #lk1 = LK.objects.all()
        lk1 = LK.objects.filter(user = request.user.get_username() )
        context = {'lk': lk1,}
        return render(request, "lk.html", context)
    return redirect("/log")

def pokupka(request):
    if request.method == "GET":
        bd = LK()
        bd.ryad = request.GET.get("ryad")
        bd.mesto = request.GET.get("mesto")
        bd.film_name= request.GET.get("film")
        bd.user = request.user.get_username()
        bd.save()
    return redirect("/lk")
    
#def index(request):
#   data = {"header": "Тебе сегодня повезет ", "message": random.randrange(0, 255, 1) }
#   return render(request, "index.html", context=data)

def searchlist(request):
    return HttpResponse("<h4>Страница поиска Демо режим</h4>")

def film(request):
    username = None
    bill = None
    film = Film.objects.all()
    username = request.user.get_username()
    if username == 'john':
        bill = "355"
    context = {'film': film, "bill" : bill}
    return render(request, "film.html", context )

def bilet(request, idfilm = 3):
    film = Film.objects.all()
    film1 = Film.objects.get(id = int(idfilm))
    
    context = {'film': film, 'film1': film1, 'idfilm': idfilm}
    return render(request, "bilet.html", context )

 
def contact(request):
    user = authenticate(username='john1', password='johnpassword')
    if user is not None:
    # the password verified for the user
        if user.is_active:
            print("User is valid, active and authenticated")
            otvet = ("User is valid, active and authenticated")
        else:
            print("The password is valid, but the account has been disabled!")
            otvet = ("The password is valid, but the account has been disabled!")
    else:
    # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        otvet = ("The username and password were incorrect.")
    return HttpResponse(otvet)

def products(request, pr):
    output = ("<h2>Product № {0}</h2>".format(pr))
    return HttpResponse(output)
 
def users(request, id, name):
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)

def page404(request):
    #return HttpResponse("<h2>Запрашиваемой страницы не существует</h2>")
    return redirect("/film")
