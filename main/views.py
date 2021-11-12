from django.shortcuts import render,HttpResponse,redirect
from .models import ToDo
from .models import ToMeet
from .models import Habits

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list= ToDo.objects.all()
    return render(request,"test.html",{"todo_list":todo_list})


def second(request):
    return HttpResponse(request,"test 2 page")

def test3(request):
    to_meeting= ToMeet.objects.all()
    return render(request,"meeting.html",{"to_meeting":to_meeting})



def add_todo(request):
    form= request.POST
    text=form["todo_text"]
    todo=ToDo(text=text)
    todo.save()
    return redirect(test)

def add_meet(request):
    form = request.POST
    text=form["ToMeet_text"]
    text2=form["ToMeet_text2"]
    meet=ToMeet(persone=text,phone_number=text2)
    meet.save()
    return redirect(test3)

def habits(request):
    habits_list = Habits.objects.all()
    return render(request,"habits.html",{"habits_list": habits_list})


def add_habits(request):
    form = request.POST
    text = form["habits_text"]
    text2=form["habits_text2"]
    habits= Habits(name=text,comment=text2)
    habits.save()
    return redirect(habits)
   
def delete_todo(request,id):
    todo= ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request,id):
    todo= ToDo.objects.get(id=id)
    todo.is_favorite=True
    todo.save()
    return redirect(test)

def close_todo(request,id):
    todo= ToDo.objects.get(id=id)
    todo.is_closed=not todo.is_closed
    todo.save()
    return redirect(test)



