from django.contrib import admin
from django.urls import path
import store.views

app_name="store"
urlpatterns = [
   path('', store.views.home, name='home'),
   path('detail/<int:pk>', store.views.detail, name='detail'),
   path('edit/', store.views.edit, name='edit'),
   path('new/', store.views.new, name='new'),
   path('create/', store.views.create, name='create'),
]