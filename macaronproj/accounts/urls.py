from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('editmypage/<int:pk>', views.editmypage, name='editmypage'),
    path('mypage/<int:pk>', views.mypage, name='mypage'),
]