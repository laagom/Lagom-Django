from django import forms
from django.contrib.auth.forms import UserCreationForm

from shortener.models import Users

# This is Form  User register
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text="Required..", label="유저명")
    full_name = forms.CharField(max_length=30, required=False, help_text="Optional..", label="이름")
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.", label="이메일")

    class Meta:
        model = Users
        fields = {
            "username", 
            "full_name",
            "email",     
            # UserCreationForm에서 선언되어 있는 명칭 
            "password1",
            "password2"
        }
