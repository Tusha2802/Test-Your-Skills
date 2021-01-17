from django.shortcuts import render,redirect,HttpResponse
from tys.forms import StuForm,UserForm,LoginForm
from tys.models import Student,User,Login,Result
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
import datetime
def a(request):
     obj=Student()
     msg=''
     btn=''
     if request.method=="POST":
          form=StuForm(request.POST)
          if form.is_valid():
               cd=form.cleaned_data;
               obj.question=cd['question']
               obj.category=cd['category']
               obj.ans1=cd['ans1']
               obj.ans2=cd['ans2']
               obj.ans3=cd['ans3']
               obj.ans4=cd['ans4']
               obj.corrans=cd['corrans']
               obj.save();
               btn=request.POST.get("btn")
               #btn1=cd['btn1']
               if(btn=="Save"):
                    msg="You have Entered Question Successfully";
                    return render(request,"tys/index.html",{'msg':msg})
            
               
     form=StuForm()
     return render(request,"tys/a.html",{'form':form})
def index(request):
     return render(request,"tys/index.html")
def cs(request):
     b=Student.objects.filter(category='1')
     return render(request,"tys/b.html",{'l':b})

def maths(request):
     b=Student.objects.filter(category='2')
     return render(request,"tys/c.html",{'l':b})

def gk(request):
     b=Student.objects.filter(category='3')
     return render(request,"tys/d.html",{'l':b})

def cstest(request):
     if request.method=="POST":
          request.session["stream"]="CS";
          return csresult(request)
     else:
          b=Student.objects.filter(category='1')
          obj=Student.objects.filter(category='1');
          paginator=Paginator(obj,2);
          page=request.GET.get('page')
          try:
               q=paginator.page(page);
          except PageNotAnInteger:
               q=paginator.page(1)
          except EmptyPage:
               q=paginator.page(paginator.num_page)
          return render(request,"tys/b1.html",{'l':q,'page':page})
          #return render(request,"tys/b1.html",{'l':b})

def csresult(request):
     count=0
     msg=HttpResponse()
     b=Student.objects.filter(category='1')
     for i in b:
          """msg.write("<p>")
          msg.write(i.id)
          msg.write(request.POST.get(str(i.id)))
          msg.write(i.corrans)
          
          msg.write("</p>")"""
          if request.POST.get(str(i.id))==i.corrans:
               count+=1
     #d=datetime.datetime.now().date()
     #d=datetime.datetime.now().time()
       
     d=datetime.date.today()
     obj=Result()
     obj.userid=request.session['uid'];
     obj.date=d;
     obj.stream=request.session['stream']
     obj.result=str(count)
     obj.save()
     
     msg.write("Result : "+str(count) + "<br>")
     msg.write("Name : " + request.session['uname'] + "<br>")
     msg.write(" id : " + str(request.session['uid']) + "<br>")
     """msg.write("D.O.T : " + str(d))
     msg.write(request.session['stream'])"""
     return msg
def removeall(request):
     r=Student.objects.all()
     r.delete()
     return render(request,"tys/index.html")
def update(request,stdid):
     r=Student.objects.get(id=stdid)
     data={'question':r.question,'category':r.category,'ans1':r.ans1,'ans2':r.ans2,'ans3':r.ans3,'ans4':r.ans4,'corrans':r.corrans}
     form=StuForm(initial=data)
     if request.method=="POST":
          w=StuForm(request.POST)
          if w.is_valid():
               cd=w.cleaned_data
               r.question=cd['question']
               r.category=cd['category']
               r.ans1=cd['ans1']
               r.ans2=cd['ans2']
               r.ans3=cd['ans3']   
               r.ans4=cd['ans4']
               r.corrans=cd['corrans']
               r.save()
               return render(request,"tys/index.html")
     else:
          return render(request,"tys/a.html",{'form':form})
def remove(request,stdid):
     r=Student.objects.get(id=stdid)
     r.delete()
     return render(request,"tys/index.html")







def a1(request):
     obj=User()
     msg=''
     x=False
     if request.method=="POST":
          form=UserForm(request.POST)
          if form.is_valid():
               cd=form.cleaned_data;
               obj.name=cd['name']
               obj.email=cd['email']
               obj.password=cd['password']
               obj.save();
               msg="You have registered successfully !"
               x=True

     else:
          form=UserForm()
     return render(request,"tys/a2.html",{'form':form,'x':x,'msg':msg})


def indexuser(request):
     msg=''
     if request.method=="POST":
          form=LoginForm(request.POST)
          if form.is_valid():
               cd=form.cleaned_data;
               btn=request.POST.get("btn")
               if(btn=="Admin"):
                    if(cd['username']=="Tushar@gmail.com" and cd['password']=="Admin"):
                         return render(request,"tys/index.html")
                    else:
                         msg="Error : Wrong Username or Password"
               else:
                    w=User.objects.get(email=cd['username'],password=cd['password'])
                    if w:
                         request.session["uid"]=w.id;
                         request.session["uname"]=w.name;
                         return render(request,"tys/usertest.html")
                         
                    else:
                         msg="Error : Wrong Details"
     else:
          form=LoginForm()
     return render(request,"tys/indexuser.html",{'form':form,'msg':msg})

def history(request):
     
     obj=Result.objects.filter(userid=request.session['uid'])
     x=request.session['uid']
     y=request.session['uname']
     return render(request,"tys/resulthistory.html",{'l':obj,'x':x,'y':y})

def homepagemenu(request):
     return render(request,"tys/homepagemenu.html")

def manageuser(request):
     obj=User.objects.all()
     return render(request,"tys/manageuser.html",{'obj':obj})

def removeuser(request,user_id):
     obj=User.objects.get(id=user_id)
     obj.delete()
     return render(request,"tys/index.html")
def aboutus(request):
     return render(request,"tys/about_us.html")

def contactus(request):
     return render(request,"tys/contact_us.html")


     



     
