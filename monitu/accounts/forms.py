from django import forms
from django.contrib.auth.forms import AuthenticationForm

from registration.forms import RegistrationFormUniqueEmail
from registration.users import UserModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

User = UserModel()


class RegisterForm(RegistrationFormUniqueEmail):
    email = forms.EmailField(label="İTÜ/Mail")
    username = forms.CharField(label="", required=False)

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("Bu eposta adresi "
                                        "ile hesap alınmıştır.")

        email_domain = self.cleaned_data['email'].split('@')[1]

        if email_domain != "itu.edu.tr":
            raise forms.ValidationError("İTÜ/Mail adresinizi giriniz.")

        self.cleaned_data['username'] = self.cleaned_data['email'] \
            .split('@')[0]

        return self.cleaned_data['email']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Hesap Oluştur'))
        self.helper.layout = Layout(
            Field('email'),
            Field('username', type="hidden"),
            Field('password1'),
            Field('password2'),
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Oturum Aç'))
        self.helper.layout = Layout(
            Field('username'),
            Field('password'),
        )
