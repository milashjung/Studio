from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.


class PhotoCategory(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

choice_list=PhotoCategory.objects.all().values_list('name','name')

class Photo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=25)
    email = models.CharField(max_length=225)
    mobile = models.CharField(max_length=40,null=True)
    age = models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)   
    experience = models.PositiveIntegerField(null=True)
    p_category = models.CharField(max_length=255,choices=choice_list,default='select')
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name



class Client(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=40,null=True)
    age = models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)
       
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name












class Photoc(models.Model):
    # sports_category = models.CharField(max_length=255,choices=choice_list,default='select')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class bphotographer(models.Model):
       
    
    photo = models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=255,default='General')
    description=models.TextField()
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.photo)

class Feedback(models.Model):
       
    
    photoName = models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.TextField()
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.photoName)




class Payment(models.Model):
    ClientId=models.PositiveIntegerField(null=True)
    CName=models.CharField(max_length=40,null=True)
    category=models.CharField(max_length=255)
    Photographer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    paidDate=models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.Photographer)


class Post(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255, )
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.CharField(max_length=255,null=True)
    Image=RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default='General')
    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})
    
    def get_absolute_url(self):
        return reverse("viewpost", kwargs={"pk": self.pk})