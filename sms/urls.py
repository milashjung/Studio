"""
by sumit kumar
written by fb.com/sumit.luv

"""
from django.contrib import admin
from django.urls import path
from appusers import views
from appusers.views import PhotoView,PhotoProfileView,AddfeedView,feedView,CategoryView1,AddbookView,CategoryListView,CategoryView,ArticleDetail2View,UpdatePostView,DeletePostView,ArticleDetailView,ViewPost,AddPostView,EditPhotoView,DeletePhotoView,\
                            \
                            EditPhotoProfileView,bookView,EditClientProfileView,ClientProfileView,PhotoCategoryView,AddPhotoView
                            
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('photoclick', views.photoclick_view),
    path('clientclick', views.clientclick_view),
    path('vbook/', bookView.as_view(template_name='site/vbook.html'), name='vbook'),
    path('vfeed/', feedView.as_view(template_name='site/vfeed.html'), name='vfeed'),

    path('admin-approve-Bookp', views.admin_approve_Bookp_view,name='admin-approve-Bookp'),
    path('approve-Bookp/<int:pk>', views.approve_Bookp_view,name='approve-Bookp'),
    path('reject-Bookp/<int:pk>', views.reject_Bookp_view,name='reject-Bookp'),


    path('adminsignup', views.admin_signup_view),
    path('clientsignup', views.client_signup_view,name='clientsignup'),
    path('photosignup', views.photo_signup_view),
    path('adminlogin', LoginView.as_view(template_name='site/adminlogin.html')),
    path('clientlogin', LoginView.as_view(template_name='site/clientlogin.html')),
    path('photologin', LoginView.as_view(template_name='site/photologin.html')),
    path('admin-approve-payment', views.admin_approve_Payment_view,name='admin-approve-payment'),
    path('approve-payment/<int:pk>', views.approve_Payment_view,name='approve-payment'),
    path('reject-payment/<int:pk>', views.reject_Payment_view,name='reject-payment'),
    path('client-payment', views.client_Payment_view,name='client-payment'),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='site/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),


    path('admin-photo', views.admin_photo_view,name='admin-photo'),
    path('adddp', views.info_view,name='adddp'),
    path('admin-add-photo', views.admin_add_photo_view,name='admin-add-photo'),
    path('admin-view-photo', views.admin_view_photo_view,name='admin-view-photo'),
    path('admin-approve-photo', views.admin_approve_photo_view,name='admin-approve-photo'),
    path('approve-photo/<int:pk>', views.approve_photo_view,name='approve-photo'),
    path('delete-photo/<int:pk>', views.delete_photo_view,name='delete-photo'),
    path('delete-photo-from-school/<int:pk>', views.delete_photo_from_school_view,name='delete-photo-from-school'),
    path('update-photo/<int:pk>', views.update_photo_view,name='update-photo'),
    path('admin-view-photo-salary', views.admin_view_photo_salary_view,name='admin-view-photo-salary'),


    path('admin-client', views.admin_client_view,name='admin-client'),
    path('admin-add-client', views.admin_add_client_view,name='admin-add-client'),
    path('admin-view-client', views.admin_view_client_view,name='admin-view-client'),
    path('delete-client-from-school/<int:pk>', views.delete_client_from_school_view,name='delete-client-from-school'),
    path('delete-client/<int:pk>', views.delete_client_view,name='delete-client'),
    path('update-client/<int:pk>', views.update_client_view,name='update-client'),
    path('admin-approve-client', views.admin_approve_client_view,name='admin-approve-client'),
    path('approve-client/<int:pk>', views.approve_client_view,name='approve-client'),
    path('admin-view-client-fee', views.admin_view_client_fee_view,name='admin-view-client-fee'),


   
    path('admin-notice', views.admin_notice_view,name='admin-notice'),



    path('photo-notice', views.photo_notice_view,name='photo-notice'),

    path('client-dashboard', views.client_dashboard_view,name='client-dashboard'),
    



    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),




    path('photo-dashboard', views.photo_dashboard_view,name='photo-dashboard'),




    path('photo/', PhotoView.as_view(template_name='site/photo.html'), name='photo'),
    
    path('add_photo/', AddPhotoView.as_view(template_name='site/add_photo.html'), name='add_photo'),
    path('edit_photo/edit/<int:pk>/', EditPhotoView.as_view(template_name='site/edit_photo.html'), name='edit_photo'),
    path('delete_photo/<int:pk>/remove', DeletePhotoView.as_view(template_name='site/delete_photo.html'), name='delete_photo'),

    path('photo_category/', PhotoCategoryView.as_view(template_name='site/photo_category.html'), name='photo_category'),
    
    path('add_post/',AddPostView.as_view(),name="add_post"),

    path('article/<int:pk>/',ArticleDetailView.as_view(),name="article-detail"),
    # path('article2/<int:pk>/',ArticleDetail2View.as_view(),name="student_articles_details"),
    path('article/<int:pk>/',ArticleDetailView.as_view(),name="teacher_articles_details"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update-post"),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="delete-post"),

    

    path('photo_profile/', PhotoProfileView.as_view(template_name='site/photo_profile.html'), name='photo_profile'),
    path('edit_photo_profile/',EditPhotoProfileView.as_view(template_name='site/edit_photo_profile.html'),name="edit_photo_profile"),
    path('client_profile/', ClientProfileView.as_view(template_name='site/client_profile.html'), name='client_profile'),
    path('edit_client_profile/',EditClientProfileView.as_view(template_name='site/edit_client_profile.html'),name="edit_client_profile"),
    path('search_photo/',views.search_photo,name="search-photo"),
    path('category/<str:cats>/',CategoryView,name="category"),
    path('category/<str:cats>/',CategoryView1,name="studentcategory"),
 
    path('article2/<int:pk>/',ArticleDetail2View.as_view(),name="client_articles_details"),
    path('category-list/',CategoryListView,name="category-list"),

    path('viewpost/',ViewPost.as_view(),name="viewpost"),
    # path('client_schedule/', ClientScheduleView.as_view(template_name='site/client_schedule.html'), name='client_schedule'),
    path('viewpost/<int:pk>/',ViewPost.as_view(),name="viewpost"),
    path('add_book/', AddbookView.as_view(template_name='site/add_book.html'), name='add_book'),
    path('add_feed/', AddfeedView.as_view(template_name='site/add_feed.html'), name='add_feed'),

]
