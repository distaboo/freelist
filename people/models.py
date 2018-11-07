from django.db import models
from django.contrib import admin
# Create your models here.
class People(models.Model):
    idvk = models.IntegerField()
    relation=models.IntegerField()
    dateChange = models.DateTimeField(auto_now_add=True)
    sex = models.IntegerField()
    city = models.IntegerField(db_index=True)
    changed = models.BooleanField(db_index=True)

    def __str__(self):
        return '{}'.format(self.id)
class ChangedPeople(models.Model):
    idvk = models.IntegerField()
    relation=models.CharField(max_length=100)
    lastRelation = models.IntegerField()
    dateChange = models.DateTimeField(auto_now_add=True)
    sex = models.IntegerField()
    city = models.IntegerField(db_index=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    photourl = models.CharField(max_length=500)
    def __str__(self):
        return '{}'.format(self.id)

admin.site.register(People)
admin.site.register(ChangedPeople)
