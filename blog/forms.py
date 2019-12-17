from django import forms
from .models import Post,Personaje
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm





class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class PersonajeForm(ModelForm):
    
    class Meta:
        model = Personaje
        fields = ['nombre','foto']
class CustomUserForm(UserCreationForm):    
    class Meta:
        model = User
        fields= ['first_name','last_name','email','username','password1','password2']
