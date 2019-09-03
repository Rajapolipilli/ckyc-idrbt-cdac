from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index,name='index'),
    path('testing/', views.testing,name='testing'),
    path('create-policy', views.ckyc_create_policy,name='create-policy'),
    path('confirm-policy/<int:pk>', views.ckyc_comfirm_policy,name='confirm-policy'),
    path('delete-policy/<int:pk>', views.ckyc_delete_policy,name='delete-policy'),

]
