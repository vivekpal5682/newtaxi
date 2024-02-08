from django.shortcuts import render, redirect
from .models import information
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST["Name"]
        pick = request.POST["Pick"]
        drop = request.POST["Drop"]
        number = request.POST["Number"]
        
        fullData = information(name=name , pick=pick, drop=drop, number=number)
        fullData.save() 
        message = """
        <p>name - """+name+""" </p>
        <p>pick location - """+pick+""" </p>
        <p>drop location - """+drop+""" </p>
        <p>number - """+number+""" </p>
        """
        send_mail("You Have New Enquery","",'pal315795@gmail.com',['omprkashpal2255@gmail.com'], fail_silently=False, html_message=message)
        return redirect('/')
    return render(request,"index.html")
    
