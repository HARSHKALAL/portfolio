from django.urls import path
from .views import Signup,homepage,Editprofile
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login


urlpatterns = [         
    path('homepage/',homepage,name="homepage"),
    path('signup/',Signup.as_view(),name="signup"),
    path('editprofile/<int:pk>',Editprofile.as_view(),name="editprofile"),

    path(
        'signin/',
        auth_views.LoginView.as_view(
        template_name='enroll/signin.html',
        success_url = '/homepage/'
        ),
        name='signin'
    ),

    path('logout_then_login/',logout_then_login,name='logout_then_login'),
   
    path(
        'change_password/',
        auth_views.PasswordChangeView.as_view(
            template_name='enroll/changepassword.html',
            success_url = '/homepage/'
        ),
        name='change_password'
    ),
]



