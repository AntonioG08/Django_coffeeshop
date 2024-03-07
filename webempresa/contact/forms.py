from django import forms


# Unlike the models, here we don't use 'verbose_name', we use 'label'
class ContactForm(forms.Form):
    """If we use 'TextInput' instead of 'EmailInput', we will lose the email pre-verification that Django provides us,
       therefore, we need to use the right widget for each specific case """
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escriba su nombre'}
    ), min_length=3, max_length=25)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Escriba su correo'}
    ), min_length=10, max_length=35)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escriba su mensaje por favor'}
    ), min_length=20, max_length=500)
