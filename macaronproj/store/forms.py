from django import forms
from .models import Macarons
from .models import Store

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Macarons
        fields = ('pic_content', 'picture', )

class ImageForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('store_pic', )