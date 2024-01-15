from django.shortcuts import render
from .models import  Contacts


# Create your views here.
def index(request):
    all_contacts = Contacts.objects.all()
    context = {'contacts': all_contacts}
    return render(request, 'app/index.html', context)
