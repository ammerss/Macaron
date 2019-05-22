from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('newsignup/', views.signupform, name="newsignup"),
    path('newlogin/', views.loginform, name="newlogin"),
]