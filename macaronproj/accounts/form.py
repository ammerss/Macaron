from django import forms
from .models import Profile

class ProfileEdit(forms.ModelForm):
    #비밀번호 확인 이랑 비밀번호가같은가? 전화번호양식이 010 어쩌구우 저쩌구우 인지
    class Mata:
        model = Profile
        fields = ['user, user_type, phone']