from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import ChangedPeople
# Create your views here.
def people_list(request,i,city):
    #proRating = request.POST.get('rating', False)
    people = ChangedPeople.objects.filter(sex=i).order_by('-dateChange')#.orderBy('dateChange')
    sex_dict = ['Девушки','Парни']
    name = [[1,'Девушки'],[2,'Парни']]
    cities = [[0,99,'Новосибирск']]
    sex = sex_dict[int(i)-1]
    current_sity = int(city)
    sity_name = cities[int(city)]
    current_sex = name[int(i)-1]

    return render(request,'people/index.html',context={'sity_name':sity_name,'cities':cities,'current_sity':current_sity,'current_sex':current_sex,'sex':sex,'name':name,'people':people})

def people_start(request):
    return HttpResponseRedirect('http://distaboo.pythonanywhere.com/1/0')