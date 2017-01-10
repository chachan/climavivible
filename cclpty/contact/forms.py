from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Correo')
    subject = forms.CharField(label='Asunto')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['subject'].widget.attrs['required'] = 'required'
        self.fields['message'].widget.attrs['required'] = 'required'
