from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.forms import ModelForm
from .models import Proveedor


class ProveedorForm(ModelForm):

    CATEGORIA_CHOICES=( 

    ("1", "Hombre"), 

    ("2", "Mujer"), 

    ("3", "Niños"), 

    ("4", "Mascotas"), 
)      

    class Meta:
        model=Proveedor
        fields=['nombre', 'razon_social', 'telefono', 'correo_electronico', 'categoria']
    
    labels = {
        'nombre':  'Nombre de representante',
        'razon_social': 'Razón social',
        'telefono': 'Teléfono de contacto',
        'correo_electronico': 'Email',
        'categoria': 'Categoría de productos',
    }

    categoria= forms.ChoiceField(choices=CATEGORIA_CHOICES)

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

            

            

            
    