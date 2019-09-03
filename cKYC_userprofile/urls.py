from django.contrib import admin
from django.urls import path,re_path
from . import views 
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

   path('ckyc-policies/',views.PolicyView,name='',),
   path('register/',views.user_signup ),
   path('signup/',views.register,name='policies',),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('login/', LoginView.as_view(template_name='registration/login.html',
      redirect_authenticated_user=True),name='login'),

   path('change-password/', views.change_password, name='change_password'),
   path('myprofile/<str:username>/', views.user_detail,name='userdetail'),
   path('myprofile/<str:username>/edit', views.user_update,name='update'),
   path('myprofile-settings/',views.user_settings,name='mysettings'),
   path('activate/<str:uid>/<str:token>', views.Activate.as_view(), name='activate'),

   
   
]

