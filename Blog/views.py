from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def About(request):
    return render(request,'about.html')



def AllData(request):
    data = Person.objects.all() #list of objects
    d = {"personData": data}
    return render(request,'all_users.html',d)


def AllBlog(request):
   data = BlogModel.objects.all()
   d = {"blog": data}
   return render(request,'index.html',d)

def BlogDetails(request, blogid):
   data = BlogModel.objects.get(id = blogid)
   d = {"blog": data}
   return render(request,'blog_data.html',d)

def AllCategory(request):
   data = Category.objects.all()
   d = {"blogCat": data}
   return render(request,'all_Category.html',d)

def Category_Detail(request,catid):
    data = Category.objects.get(id = catid)
    blogs = BlogModel.objects.filter(cat = data)
    d = {"blogs": blogs}
    return render(request,'cat_details.html',d)

def AddCategory(request):
      if request.method == 'POST':
          dic = request.POST
          c = dic['cname']
          Category.objects.create(name = c)
          return redirect('Category')
      return render(request,'add_cat.html')

#  Login System
from django.contrib.auth import authenticate,login,logout


def SignUp(request):
    error = False
    if request.method == "POST":
        d = request.POST
        full = d['fname'].split()
        first = full[0]
        last = full[1]
        mob = d['mob']
        em = d['email']
        u = d['uname']
        p = d['pwd']
        i = request.FILES['img']
        user = User.objects.filter(username = u)
        if user:
            error = True
        else:
            userdata = User.objects.create_user(username=u, password=p,
                                                email=em, first_name=first,
                                                last_name=last)
            UserDetail.objects.create(user=userdata, image=i, mobile=mob)
            return redirect('login')


    return render(request,'signup.html')


def LoginForm(request):
    if request.method == "POST":
        dic = request.POST
        u = dic['user']
        p = dic['pwd']
        user = authenticate(username = u , password = p)
        if user:
              login(request,user)
              if request.user.is_staff:
                  return redirect('adminpanel')
              return redirect('userpanel')
        else:
              return HttpResponse("user not found")
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('allblogs')

# if user is super user
def AdminPanel(request):
    return render(request,'adminpanel.html')


# Normal user
def Userpanel(request):
    if not request.user.is_authenticated:
        return redirect('login')
    userblogs = BlogModel.objects.filter(user = request.user)
    userdata = UserDetail.objects.get(user = request.user )
    d = {"userblogs":userblogs, "userdata":userdata}
    return render(request, 'userpanel.html',d)



from datetime import date
def AddBlog(request):
      if not request.user.is_authenticated:
          return redirect("login")
      allcategory = Category.objects.all()
      d = {"allcategory":allcategory}

      if request.method == "POST":
          dic = request.POST
          catid = dic['cat']
          catdata = Category.objects.get(id = catid)
          title = dic['title']
          str = dic['short']
          long = dic['long']
          img = request.FILES['img']
          td = date.today()
          userdata = request.user
          BlogModel.objects.create(user = userdata,
                                   cat = catdata,
                                   title = title,
                                   short_des = str,
                                   long_des = long,
                                   date = td,
                                   image = img
                                   )
          return redirect('CatDetails', catid)
      return render(request,'add_blog.html',d)
