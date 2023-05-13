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


# This is Form Login Form
class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "이메일"})
    )
    password = forms.CharField(
        max_length=30, required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "패스워드"})
    )
    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input", "id": "_loginRememberMe"}),
        required=False,
        disabled=False,
    )