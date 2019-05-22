from django.contrib import admin
from django.urls import path
import store.views
from django.conf import settings
from django.conf.urls.static import static


app_name="store"
urlpatterns = [
   path('', store.views.home, name='home'),
   path('detail/<int:pk>', store.views.detail, name='detail'),
   path('detail/<int:pk>/edit/', store.views.edit, name='edit'),
   path('new/', store.views.new, name='new'),
   path('create/', store.views.create_store, name='create_store'),
   # path('upload_pic/<int:pk>', store.views.upload_pic, name='upload_pic'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)