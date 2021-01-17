from django import forms
from tys.models import Student,User,Login

class StuForm(forms.ModelForm):
     class Meta:
          model=Student;
          fields="__all__";
          
class UserForm(forms.ModelForm):
     class Meta:
          model=User;
          fields="__all__"
     
class LoginForm(forms.ModelForm):
     class Meta:
          model=Login
          fields="__all__"

