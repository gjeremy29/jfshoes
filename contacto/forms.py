from django import forms

class ContactForm(forms.Form):
    nombres = forms.CharField(max_length=100, required=True,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo = forms.EmailField(required=True,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    celular = forms.CharField(max_length=13, required=True,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    ruc = forms.CharField(max_length=13, required=True,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=50, required=True, label='Dirección',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
    aceptar_condiciones = forms.BooleanField(required=True, label='Cuenta con tienda física o en línea')
