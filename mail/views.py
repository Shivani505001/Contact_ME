from django.shortcuts import render,HttpResponse
from .models import contact
# Create your views here.
def home(requests):
    if requests.method=='POST':
        user=contact()
        Name=requests.POST.get('name')
        Email=requests.POST.get('email')
        msg=requests.POST.get('message')
        
        user.name=Name
        user.email=Email
        user.message=msg
        user.save()
        return HttpResponse('Thank you')
    return render (requests,'index.html')
