from django.shortcuts import render
from django.http import HttpResponse
from .models import ChangedPeople
# Create your views here.
def people_list(request):
    people = ChangedPeople.objects.filter(sex=1).order_by('dateChange')#.orderBy('dateChange')
    return render(request,'people/index.html',context={'people':people})