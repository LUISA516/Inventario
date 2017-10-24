from django import forms


class RegistroForm(forms.Form):
	Codigo = forms.CharField(max_length=100)
	Referencia = forms.CharField(max_length=100)
	cantidad = forms.CharField(max_length=100)
	fecha_registro = forms.DateTimeField()

'''
from django import forms
from registro.models import Registro

class RegistroForm(forms.ModelForm):

	class Meta:   #para indicar de que modelo se va a crear el formulario
		model = Registro

		fields = [
           'id_registro',
           'id_producto',
           'nombre_registro',
           'cantidad_registro',
           'fecha_registro',
           
		]
		labels = {
	        'id_registro' : 'Codigo',
	        'id_producto': 'Producto',
	        'nombre_registro' : 'Nombre',
	        'cantidad_registro' : 'Cantidad',
	        'fecha_registro' : 'Fecha de registro',
	        
		}
		widgets = {
		'id_registro': forms.TextInput(attrs={'class':'form-control'}),
        'id_producto': forms.Select(attrs={'class':'form-control'}),
        'nombre_registro': forms.TextInput(attrs={'class':'form-control'}),
        'cantidad_registro': forms.TextInput(attrs={'class':'form-control'}),
        'fecha_registro': forms.TextInput(attrs={'class':'form-control'}),

		}
'''