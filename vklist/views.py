from django.http import HttpResponse

def nsk(request,s):
    return HttpResponse('<h1>'+str(s)+'<h1>')