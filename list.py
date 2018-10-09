import requests
import vk
import time

import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vklist.settings")
django.setup()
from people.models import People
access_token = '8dce90ac8dce90ac8dce90ac3e8dabb4f588dce8dce90acd68df0fb950b466da7f00420'
session = vk.Session(access_token=access_token)
api = vk.API(session)
def scrab(first,count,city):
    users = [i for i in range(first,first+count)]
    r =api.users.get(user_ids=users,v='5.52',fields = ['relation','city','sex'])
    #print(r[0])
    users_final = []
    for user in r:
        if ('city' in user) and ('relation' in user) :
            if user.get('city').get('id')==city :
                users_final.append([user.get('id'),user.get('relation')])
                People.objects.create(idvk = user.get('id'),relation = user.get('relation'),changed = False,city = city,sex = user.get('sex') )
    return users_final

startTime = time.time()
last = People.objects.get(id = People.objects.all().count()).idvk + 1
for i in range(100000):
    try:
        scrab(last+1000*i,1000,99)
    except: print('Error')
    print(i)
#scrab(1,100,99)
print(time.time() - startTime)
print(People.objects.get(id = People.objects.all().count()).idvk)
def getJson(url,data = None):
    response = requests.get(url,params=data)
    response = response.json()
    print(response)
    return response

#getJson("https://api.vk.com/method/users.get",{ 'user_id':[210700286,1],'v':'5.52' , 'access_token': access_token})

#api.search(q = 'Денис Грязнов',v = '5.0')