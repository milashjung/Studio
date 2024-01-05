from django import forms
from django.contrib.auth.models import User
from . import models
from django.forms import widgets
from .models import Feedback, Photoc,PhotoCategory,Post, bphotographer

from django.contrib.auth.forms import UserCreationForm,UserChangeForm



choice_list=PhotoCategory.objects.all().values_list('name','name')
#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']



class ClientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class ClientForm(forms.ModelForm):
    class Meta:
        model=models.Client
        fields=['address','email','mobile','age','status']
        


class PhotoUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class PhotoForm(forms.ModelForm):
    class Meta:
        model=models.Photo
        fields=['address','email','mobile','age','status','experience','p_category']







class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','category','Image','price')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is title placeholder'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'Image':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
        }









class PhotoCategoryPostForm(forms.ModelForm):
    class Meta:
        model=PhotoCategory
        fields=('name',)

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }


choice_list=PhotoCategory.objects.all().values_list('name','name')

class PhotoPostForm(forms.ModelForm):
    class Meta:
        model=Photoc
        fields=('title','author','body','description')

        widgets={
            # 'sports_category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'this is title placeholder'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }   

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model=Photoc
        fields=('title','body','description')

        widgets={
            # 'sports_category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }  
        









class EditPhotoProfileForm(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    date_joined=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password',
                'last_login','date_joined')

class EditClientProfileForm(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    date_joined=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password',
                'last_login','date_joined')




class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','author','category','Image','price')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is title placeholder'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'Image':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
        }

class bpPostForm(forms.ModelForm):
    class Meta:
        model=bphotographer
        fields=('photo','description','category')

        widgets={
            'photo':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),

            'description':forms.Textarea(attrs={'class':'form-control'}),
            
        }   

class feedPostForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=('photoName','message','email')

        widgets={
            'photoName':forms.Select(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),

            'email':forms.TextInput(attrs={'class':'form-control'}),
            
        }      



class PaymentForm(forms.ModelForm):
    # DrivingId=forms.ModelChoiceField(queryset=models.Driving.objects.all().filter(status=True),empty_label="Select Driving School To Which You Want To Pay", to_field_name="user_id")
    
    ClientId=forms.ModelChoiceField(queryset=models.Client.objects.all().filter(status=True),empty_label="Client Name ", to_field_name="user_id")
    class Meta:
        model=models.Payment
        fields=['status','amount','CName','category','Photographer']


class ClientPaymentForm(forms.ModelForm):
    
    class Meta:
        model=models.Payment
        fields=['status','amount','CName','category','Photographer']