import requests
import vk
import time

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vklist.settings")
django.setup()
from people.models import People
from people.models import ChangedPeople

access_token = '8dce90ac8dce90ac8dce90ac3e8dabb4f588dce8dce90acd68df0fb950b466da7f00420'
session = vk.Session(access_token=access_token)
api = vk.API(session)


def update():
    for i in range(People.objects.all().count() // 1000 + 1):
        try:
            time.sleep(0.5)
            people = []
            # print(People.objects.all().count()//1000+1)
            # print(people)
            m = People.objects.all()[i * 1000:1000 * i + 1000]
            # print(ChangedPeople.objects.all())
            for k in m:
                people.append(k.idvk)
            # print(people)

            r = api.users.get(user_ids=people, v='5.52',
                              fields=['relation', 'city', 'sex', 'photo_50', 'first_name', 'last_name'], timeout=60)
            print(i)
            # print(str(m[0].idvk)+' '+str(r[0].get('id')))
            # for k, j in zip(r, m):
            #    if (k.get('relation') != j.relation) :
            #           print(str(k.get('relation'))+'  '+str(j.relation))
            #            print(str(k.get('id')) + ' ' + str(j.idvk))
            #            print(str(('relation' in k)))
            #            print(k)

            for k, j in zip(r, m):
                if (k.get('relation') != j.relation) and ('relation' in k):
                    # print(k.get('relation'))
                    # print(j.relation)
                    try:
                        ChangedPeople.objects.create(lastRelation=j.relation, idvk=k.get('id'),
                                                     relation=int(k.get('relation')), city=k.get('city').get('id'),
                                                     sex=k.get('sex'), name=k.get('first_name'),
                                                     lastname=k.get('last_name'), photourl=k.get('photo_50'))
                    except:
                        print('err')
                    j.relation = k.get('relation')
                    j.save()
        except (ConnectionError, TimeoutError) as e:
            print(e)


update()
