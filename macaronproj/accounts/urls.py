from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
<<<<<<< HEAD
]

    # path('newsignup/', views.signupform, name="newsignup"),
    # path('newlogin/', views.loginform, name="newlogin"),
=======
    path('editmypage/<int:pk>', views.editmypage, name='editmypage'),
    path('mypage/<int:pk>', views.mypage, name='mypage'),
]
>>>>>>> 00a29c4fff0b54a9642fc91360022187a7c3db3d
