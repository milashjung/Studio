from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.core.mail import send_mail

from .forms import PhotoPostForm,feedPostForm,bpPostForm,PostForm,EditForm,PhotoEditForm,\
EditPhotoProfileForm,EditClientProfileForm,PhotoCategory, PhotoCategoryPostForm

from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from .models import Photoc,Feedback,Post, bphotographer

from django.urls.base import reverse_lazy

from django.contrib.auth.models import User


class ViewPost(ListView):
    model=Post
    template_name="site/viewpost.html"
    def get_context_data(self,*args,**kwargs):
        cat_menu=PhotoCategory.objects.all()
        context=super(ViewPost, self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context
    
    def get_queryset(self):
            user = self.request.user
            return Post.objects.filter(author=user)

#ScheduleView
def CategoryView(request,cats):
    category_post=Post.objects.filter(category=cats)
    return render(request,'site/categoriesphoto.html',{'cats':cats.title(),'category_post':category_post})

class ArticleDetailView(DetailView):
    model=Post
    template_name='site/articles_details.html'
    def get_context_data(self,*args,**kwargs):
        cat_menu=PhotoCategory.objects.all()
        context=super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context

class ArticleDetail2View(DetailView):
    model=Post
    template_name='site/client_articles_details.html'
    def get_context_data(self,*args,**kwargs):
        cat_menu=PhotoCategory.objects.all()
        context=super(ArticleDetail2View,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context
class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name="site/update_post.html"

class DeletePostView(DeleteView):
    model=Post
    template_name="site/delete_post.html"
    success_url=reverse_lazy('')








def CategoryListView(request):
    cat_menu_list=PhotoCategory.objects.all()
    return render(request,'site/category_list.html',{'cat_menu_list':cat_menu_list})



#EventView





class PhotoProfileView(ListView):
    model=User
    template_name='photo_profile.html'

class EditPhotoProfileView(UpdateView):
    form_class=EditPhotoProfileForm
    template_name='edit_photo_profile.html'
    success_url=reverse_lazy('photo_profile')

    def get_object(self):
        return self.request.user

class ClientProfileView(ListView):
    model=User
    template_name='client_profile.html'

class EditClientProfileView(UpdateView):
    form_class=EditClientProfileForm
    template_name='edit_client_profile.html'
    success_url=reverse_lazy('client_profile')

    def get_object(self):
        return self.request.user



def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'site/index.html')


class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name="site/add_post.html"

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'site/adminclick.html')


def photoclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'site/photoclick.html')



def clientclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'site/clientclick.html')





def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'site/adminsignup.html',{'form':form})




def client_signup_view(request):
    form1=forms.ClientUserForm()
    form2=forms.ClientForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.ClientUserForm(request.POST)
        form2=forms.ClientForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_client_group = Group.objects.get_or_create(name='CLIENT')
            my_client_group[0].user_set.add(user)

        return HttpResponseRedirect('clientlogin')
    return render(request,'site/clientsignup.html',context=mydict)


def photo_signup_view(request):
    form1=forms.PhotoUserForm()
    form2=forms.PhotoForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.PhotoUserForm(request.POST)
        form2=forms.PhotoForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_photo_group = Group.objects.get_or_create(name='PHOTO')
            my_photo_group[0].user_set.add(user)

        return HttpResponseRedirect('photologin')
    return render(request,'site/photosignup.html',context=mydict)







def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_photo(user):
    return user.groups.filter(name='PHOTO').exists()
def is_client(user):
    return user.groups.filter(name='CLIENT').exists()


def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_photo(request.user):
        accountapproval=models.Photo.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('photo-dashboard')
        else:
            return render(request,'site/photo_wait_for_approval.html')
    elif is_client(request.user):
        accountapproval=models.Client.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('client-dashboard')
        else:
            return render(request,'site/client_wait_for_approval.html')


def CategoryView1(request,cats):
    category_post=Post.objects.filter(category=cats)
    return render(request,'site/clientcategories.html',{'cats':cats.title(),'category_post':category_post})


class AddbookView(CreateView):
    model=bphotographer
    form_class=bpPostForm
    template_name="add_book.html"
    success_url=reverse_lazy('client-payment')


class AddfeedView(CreateView):
    model=bphotographer
    form_class=feedPostForm
    template_name="add_feed.html"
    success_url=reverse_lazy('client-dashboard')

#for dashboard of adminnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn(by sumit)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    photocount=models.Photo.objects.all().filter(status=True).count()
    pendingphotocount=models.Photo.objects.all().filter(status=False).count()

    clientcount=models.Client.objects.all().filter(status=True).count()
    pendingclientcount=models.Client.objects.all().filter(status=False).count()

    
    
    photo=models.Photoc.objects.all().count()
    
    

    
    mydict={
        'photocount':photocount,
        'pendingphotocount':pendingphotocount,

        'clientcount':clientcount,
        'pendingclientcount':pendingclientcount,

        
        
        'photo':photo,
        

    }

    return render(request,'site/admin_dashboard.html',context=mydict)







#for photo sectionnnnnnnn by adminnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn(by sumit)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_photo_view(request):
    return render(request,'site/admin_photo.html')

@login_required(login_url='photologin')
@user_passes_test(is_photo)
def info_view(request):
    return render(request,'site/info.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_photo_view(request):
    form1=forms.PhotoUserForm()
    form2=forms.PhotoForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.PhotoUserForm(request.POST)
        form2=forms.PhotoForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_photo_group = Group.objects.get_or_create(name='PHOTO')
            my_photo_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-photo')
    return render(request,'site/admin_add_photo.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_photo_view(request):
    photos=models.Photo.objects.all().filter(status=True)
    return render(request,'site/admin_view_photo.html',{'photos':photos})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_photo_view(request):
    photos=models.Photo.objects.all().filter(status=False)
    return render(request,'site/admin_approve_photo.html',{'photos':photos})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_photo_view(request,pk):
    photo=models.Photo.objects.get(id=pk)
    photo.status=True
    photo.save()
    return redirect(reverse('admin-approve-photo'))


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_photo_view(request,pk):
    photo=models.Photo.objects.get(id=pk)
    user=models.User.objects.get(id=photo.user_id)
    user.delete()
    photo.delete()
    return redirect('admin-approve-photo')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_photo_from_school_view(request,pk):
    photo=models.Photo.objects.get(id=pk)
    user=models.User.objects.get(id=photo.user_id)
    user.delete()
    photo.delete()
    return redirect('admin-view-photo')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_photo_view(request,pk):
    photo=models.Photo.objects.get(id=pk)
    user=models.User.objects.get(id=photo.user_id)

    form1=forms.PhotoUserForm(instance=user)
    form2=forms.PhotoForm(instance=photo)
    mydict={'form1':form1,'form2':form2}

    if request.method=='POST':
        form1=forms.PhotoUserForm(request.POST,instance=user)
        form2=forms.PhotoForm(request.POST,instance=photo)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            return redirect('admin-view-photo')
    return render(request,'site/admin_update_photo.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_photo_salary_view(request):
    photos=models.Photo.objects.all()
    return render(request,'site/admin_view_photo_salary.html',{'photos':photos})



class PhotoCategoryView(CreateView):
    model=PhotoCategory
    form_class=PhotoCategoryPostForm
    template_name='photo_category.html'
    success_url=reverse_lazy('add_sports')

class AddPhotoView(CreateView):
    model=Photoc,PhotoCategory
    form_class=PhotoPostForm
    template_name="add_photo.html"
    success_url=reverse_lazy('photo')

class EditPhotoView(UpdateView):
    model=Photoc
    form_class=PhotoEditForm
    template_name='edit_Photo.html'
    success_url=reverse_lazy('photo')

class DeletePhotoView(DeleteView):
    model=Photoc
    template_name="delete_photo.html"
    success_url=reverse_lazy('Photo')

class PhotoView(ListView):
    model=Photoc
    template_name='photo.html'
class PhotoCategoryView(CreateView):
    model=PhotoCategory
    form_class=PhotoCategoryPostForm
    template_name='photo_category.html'
    success_url=reverse_lazy('add_photo')


#for client by adminnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn(by sumit)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_client_view(request):
    return render(request,'site/admin_client.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_client_view(request):
    form1=forms.ClientUserForm()
    form2=forms.ClientForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.ClientUserForm(request.POST)
        form2=forms.ClientForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_client_group = Group.objects.get_or_create(name='CLIENT')
            my_client_group[0].user_set.add(user)
        else:
            print("form is invalid")
        return HttpResponseRedirect('admin-client')
    return render(request,'site/admin_add_client.html',context=mydict)

class bookView(ListView):
    model=bphotographer
    template_name='vbook.html'
    def get_queryset(self):
        user = self.request.user
        return bphotographer.objects.filter(photo=user)


class feedView(ListView):
    model=Feedback
    template_name='vfeed.html'
    def get_queryset(self):
        user = self.request.user
        return Feedback.objects.filter(photoName=user)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_client_view(request):
    clients=models.Client.objects.all().filter(status=True)
    return render(request,'site/admin_view_client.html',{'clients':clients})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_client_from_school_view(request,pk):
    client=models.Client.objects.get(id=pk)
    user=models.User.objects.get(id=client.user_id)
    user.delete()
    client.delete()
    return redirect('admin-view-client')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_client_view(request,pk):
    client=models.Client.objects.get(id=pk)
    user=models.User.objects.get(id=client.user_id)
    user.delete()
    client.delete()
    return redirect('admin-approve-client')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_client_view(request,pk):
    client=models.Client.objects.get(id=pk)
    user=models.User.objects.get(id=client.user_id)
    form1=forms.ClientUserForm(instance=user)
    form2=forms.ClientForm(instance=client)
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.ClientUserForm(request.POST,instance=user)
        form2=forms.ClientForm(request.POST,instance=client)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            return redirect('admin-view-client')
    return render(request,'site/admin_update_client.html',context=mydict)



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_client_view(request):
    clients=models.Client.objects.all().filter(status=False)
    return render(request,'site/admin_approve_client.html',{'clients':clients})

@login_required(login_url='photologin')
@user_passes_test(is_photo)
def admin_approve_Bookp_view(request):
    #those whose approval are needed
    bookps=models.bphotographer.objects.all().filter(status=False)
    return render(request,'site/admin_approve_Bookp.html',{'bookps':bookps})

@login_required(login_url='photologin')
@user_passes_test(is_photo)
def approve_Bookp_view(request,pk):
    bookp=models.bphotographer.objects.get(id=pk)
    bookp.status=True
    bookp.save()
    return redirect(reverse('admin-approve-Bookp'))

@login_required(login_url='photologin')
@user_passes_test(is_photo)
def reject_Bookp_view(request,pk):
    bookp=models.bphotographer.objects.get(id=pk)
    bookp.delete()
    return redirect('admin-approve-Bookp')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_client_view(request,pk):
    clients=models.Client.objects.get(id=pk)
    clients.status=True
    clients.save()
    return redirect(reverse('admin-approve-client'))

@login_required(login_url='photologin')
@user_passes_test(is_photo)
def admin_approve_Payment_view(request):
    #those whose approval are needed
    Payment=models.Payment.objects.all().filter(status=False)
    return render(request,'site/admin_approve_payment.html',{'Payment':Payment})

@login_required(login_url='photologin')
@user_passes_test(is_photo)
def approve_Payment_view(request,pk):
    Payment=models.Payment.objects.get(id=pk)
    Payment.status=True
    Payment.save()
    return redirect(reverse('admin-approve-payment'))


@login_required(login_url='photologin')
@user_passes_test(is_photo)
def reject_Payment_view(request,pk):
    Payment=models.Payment.objects.get(id=pk)
    Payment.delete()
    return redirect('admin-approve-payment')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_client_fee_view(request):
    clients=models.Client.objects.all()
    return render(request,'site/admin_view_client_fee.html',{'clients':clients})

def client_Payment_view(request):
    PaymentForm=forms.ClientPaymentForm()
    client=models.Client.objects.get(user_id=request.user.id) #for profile picture of client in sidebar
    message=None
    mydict={'PaymentForm':PaymentForm,'message':message}
    if request.method=='POST':
        PaymentForm=forms.ClientPaymentForm(request.POST)
        if PaymentForm.is_valid():
            
            pay_for=request.POST.get('pay_for')
            amount=request.POST.get('amount')

            Payment=PaymentForm.save(commit=False)
           
          
            Payment.ClientId=request.user.id #----user can choose any client but only their info will be stored
            
            Payment.status=False
            Payment.save()
        return HttpResponseRedirect('client-dashboard')
    return render(request,'site/payment.html',context=mydict)





#attendance related viewwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww(by sumit)
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_attendance_view(request):
    return render(request,'site/admin_attendance.html')











#fee related view by adminnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn(by sumit)
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_fee_view(request):
    return render(request,'site/admin_fee.html')










#notice related viewsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss(by sumit)
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_notice_view(request):
    form=forms.NoticeForm()
    if request.method=='POST':
        form=forms.NoticeForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.by=request.user.first_name
            form.save()
            return redirect('admin-dashboard')
    return render(request,'site/admin_notice.html',{'form':form})








#for TEACHER  LOGIN    SECTIONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN(by sumit)
@login_required(login_url='photologin')
@user_passes_test(is_photo)
def photo_dashboard_view(request):
    photodata=models.Photo.objects.all().filter(status=True,user_id=request.user.id)
    
    mydict={
        
        'mobile':photodata[0].mobile,
        
        
    }
    return render(request,'site/photo_dashboard.html',context=mydict)



@login_required(login_url='photologin')
@user_passes_test(is_photo)
def photo_attendance_view(request):
    return render(request,'site/photo_attendance.html')








@login_required(login_url='photologin')
@user_passes_test(is_photo)
def photo_notice_view(request):
    form=forms.NoticeForm()
    if request.method=='POST':
        form=forms.NoticeForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.by=request.user.first_name
            form.save()
            return redirect('photo-dashboard')
        else:
            print('form invalid')
    return render(request,'site/photo_notice.html',{'form':form})







#FOR client AFTER THEIR Loginnnnnnnnnnnnnnnnnnnnn(by sumit)
@login_required(login_url='clientlogin')
@user_passes_test(is_client)
def client_dashboard_view(request):
    clientdata=models.Client.objects.all().filter(status=True,user_id=request.user.id)
    
    mydict={
        'email':clientdata[0].email,
        'mobile':clientdata[0].mobile,
        'age':clientdata[0].age,
        #'notice':notice
    }
    return render(request,'site/client_dashboard.html',context=mydict)






def search_photo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        title = models.Post.objects.filter(title__contains=searched)
        return render(request,'site/search_photo.html',{'searched': searched,'title':title})
    else:
        return  render(request,
        'site/search_photo.html',
        {})






# for aboutus and contact ussssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss (by sumit)
def aboutus_view(request):
    return render(request,'site/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'site/contactussuccess.html')
    return render(request, 'site/contactus.html', {'form':sub})
