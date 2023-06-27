from django.shortcuts import render, HttpResponse
from Home.models import contact

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        roll = request.POST.get("roll")
        semester = request.POST.get("semester")
        gender = request.POST.get("gender")
        vote = request.POST.get("vote")
        Contact = contact(name=name, phone=phone, email=email,
                          roll=roll, semester=semester, gender=gender, vote=vote)
        Contact.save()
    return render(request, 'index.html')
