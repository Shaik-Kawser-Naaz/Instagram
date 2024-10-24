from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from insta.models import post
# Create your views here.
@login_required(login_url="/admin")
def create(request):
    if request.method=="POST":
        image=request.FILES['image']
        capt=request.POST.get('cap')
        obj=post(user=request.user,photo=image,caption=capt)
        obj.save()
    return render(request,'create.html')
def home(request):
    obj=post.objects.all()
    return render(request,'index.html',{'posts':obj})