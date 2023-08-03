from django.shortcuts import render,redirect,HttpResponse
from banking.models import Bank
from threading import *
# Create your views here.
# def home(request):
#     return render(request,'index.html')
# global obj
# obj = Semaphore(1) 
global dep #take is var ko har func mien use kr skyn
dep=Semaphore(2)
def setaccount(request):
    if request.method=="POST":
        accountnumber=request.POST['accountnumber']#name in our templte
        username=request.POST['username']
        balance=request.POST['balance']
        withdraw=request.POST['withdraw']
        deposit=request.POST['deposit']

        data=Bank(accountnumber=accountnumber,username=username,balance=balance,withdraw=withdraw,deposit=deposit)
        data.save()
        return redirect('/withdraw')
    else:
        return render(request,"insert.html")   
#obj.release()   
    
def withdraw(request,pk):
    print('func of with')
    dep.acquire()#2--1--0
    if request.method=="POST":
        #print("post hua")
        dep.release()#+1
        dep.release()#+2
        withdraw=int(request.POST["withdraw"])
        data=Bank.objects.get(id=pk)
        if data.balance >= withdraw:
            data.balance-=withdraw
            data.save()
            #return get(request)
            #return render(request,"index.html",{"bank":data})
            return redirect("/")
        else:
            return HttpResponse("pese kam hain")
    else:
        #print("ye click krne se pehle ka hai")
        bank = Bank.objects.get(id=pk)
        return render(request,"withdraw.html",{"bank":bank})
        #
        
   
def get(request):
    print(dep._value)

        
    if dep._value<2:
        return redirect("/busy")
        
    else:
        bank =Bank.objects.get()
        return render(request,"index.html",{"bank":bank})
    

def deposit(request,pk):
    #print(obj._value)
    dep.acquire()#2---1---0
    if request.method =="POST":
        dep.release()
        dep.release()
        deposit=int(request.POST['deposit'])
        members=Bank.objects.get(id=pk)
        members.balance+=deposit
        members.save()
        return redirect("/")
        #return render(request,"deposit.html",{"bank":members})

    else:
        bank=Bank.objects.get(id=pk)
        return render(request,"deposit.html",{"bank":bank})

def busy(request):
    return render(request,"busy.html")