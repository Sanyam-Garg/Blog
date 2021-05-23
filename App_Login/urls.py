from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('sign-up/', views.sign_up, name = 'sign_up'),
    path('login/', views.login_page, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('update-profile/', views.update_profile, name = 'update_profile'),
    path('password/', views.change_password, name = 'change_password'), # This slug is default
    path('add-profile-pic/', views.add_profile_pic, name = 'add_profile_pic'),
    path('change-profile-pic/', views.change_profile_pic, name = 'change_profile_pic'),
]
