from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import book
from .forms import BookCreate
from math import ceil
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
import re
from .forms import SignUpForm
# Create your views here.

def loginpage(request):
    if request.method == "POST":
        roll_no = request.POST['roll']
        passw = request.POST['password']
        print(roll_no)
        print(passw)
        user = authenticate(username=roll_no,password=passw)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            msg = "Invalid credential"
            return render(request,"login.html",{'msg':msg})
    return render(request,"login.html")
def registration(request):
    fm = SignUpForm
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')      
    return render(request,"register.html",{"fm":fm})

def logoutpage(request):
    logout(request)
    return redirect('/')
def index(request):
    shelf=book.objects.all()
    paginator=Paginator(shelf,5)
    page=request.GET.get('page')
    shelf=paginator.get_page(page)
    return render(request,'index.html',{'shelf':shelf})

def upload(request):
    upload=BookCreate()
    if  request.method == 'POST':
        upload = BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, relaod on <a href = "{{url:'index'}}"reload</a>""")
    else:
        return render(request,'upload_form.html',{'upload_form':upload})
    
def update_book(request,book_id):
    book_id=int(book_id)
    try:
        book_sel=book.objects.get(id = book_id)
    except book.DoesNotExist:
        return redirect('index')
    if request.method == 'POST':
        book_form = BookCreate(request.POST,request.FILES,instance=book_sel)
    else:
        book_form = BookCreate(None,instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request,'upload_form.html',{'upload_form':book_form})
    
def delete_book(request,book_id):
    book_id=int(book_id)
    try:
        book_sel=book.objects.get(id=book_id)
    except book.DoesNotExist:
        redirect('index')
    book_sel.delete()
    return redirect('index')

def download(request,path):
    filepath=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exist(filepath):
        with open(filepath,'rb')as file:
            response=HttpResponse(file.read())
            response['Content-Disposition']='inline;filename='+os.path.basename(filepath)
            return response
    raise Http404

def search(request):
    data=request.GET['search']
    print(data)
    if len(data)>70 :
        cover=book.objects.none()
    else:
        filename1=book.objects.filter(file__icontains=data)
        filename2=book.objects.filter(name__icontains=data)
        filename3=book.objects.filter(auther__icontains=data)
        filename4=book.objects.filter(discribe__icontains=data) 
        cover=filename3.union(filename2,filename4,filename1) 
    return render(request,'search.html',{'query':data,'allsearch':cover})
    
