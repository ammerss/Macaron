from django.contrib import admin
from django.urls import path
import store.views



app_name="store"
urlpatterns = [   
   path('', store.views.home, name='home'),
   path('detail/<int:pk>', store.views.detail, name='detail'),
   path('detail/<int:pk>/edit/', store.views.edit, name='edit'),
   path('new/', store.views.new, name='new'),
   path('create/', store.views.create_store, name='create_store'),
   path('mystores/<int:user_id>/editmystore/<int:store_id>/', store.views.editmystore,name='editmystore'),
   path('mystores/<int:user_id>/', store.views.mystores, name='mystores'),
   path('detail/<int:store_id>/delete/<int:macarons_id>',store.views.delete, name='delete'),
   # path('upload_pic/<int:pk>', store.views.upload_pic, name='upload_pic'),
]