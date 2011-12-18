from django.db import models

class User(models.Model):
     username=models.CharField(max_length=50)
     password=models.CharField(max_length=50)
     email=models.EmailField(max_length=50)
     created=models.DateTimeField(auto_now=False,auto_now_add=True)
     def __unicode__(self):
          return self.username+" "+self.password+" "+self.email
     

class List(models.Model):
     user_id=models.ForeignKey(User)
     item=models.CharField(max_length=150)
     priority=models.IntegerField()
     isComplete=models.IntegerField(default=0)
     created=models.DateTimeField(auto_now=False,auto_now_add=True)
     def __unicode__(self):
          return self.item
     
     
# Create your models here.
