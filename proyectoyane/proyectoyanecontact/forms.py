from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(
        label="Contenido",
        required=True,
        widget=forms.Textarea,
    )
