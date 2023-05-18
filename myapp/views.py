from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 時間函數
from datetime import datetime

import random

def students(request):
    std1 = {"name": "111", "sid": "110913111", "age": 11}
    std2 = {"name": "222", "sid": "110913222", "age": 22}
    std3 = {"name": "333", "sid": "110913333", "age": 33}
    stds = [std1, std2, std3]
    return render(request, 'std.html', locals())

def hello(request):
    # return HttpResponse("Hello World")
    return render(request, 'hello.html')
    
def hello1(request,username):
    now = datetime.now()
    return render(request, 'hello1.html',locals())

times = 0
    
def hello2(request,username):
    global times
    times = times + 1
    local_times = times
    now = datetime.now()
    dicenum1 = random.randint(1,6)
    dicenum2 = random.randint(1,6)
    dicenum3 = random.randint(1,6)
    dict1 = {"dice1": dicenum1, "dice2": dicenum2, "dice3": dicenum3}
    score = random.randint(0,100)
    return render(request, 'hello2.html', locals())
    #{"username": "test123", "now": now, "dict1": dict1}
