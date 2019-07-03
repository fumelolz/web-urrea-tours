from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label="Nombre",required=True,widget=forms.TextInput( attrs={'class':'common-input mb-20 form-control','placeholder':'Escribe tu Nombre'} ),min_length=3,max_length=100)
	email = forms.EmailField(label="Email",required=True,widget=forms.EmailInput( attrs={'class':'common-input mb-20 form-control','placeholder':'Escribe tu Correo'} ),min_length=3,max_length=100)
	content = forms.CharField(label="Contenido",required=True,widget=forms.Textarea( attrs={'class':'common-textarea form-control','rows':3,'placeholder':'Escribe tu mensaje'}),min_length=3,max_length=1000)