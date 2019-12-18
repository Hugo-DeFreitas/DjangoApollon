from django import forms
from django.forms import Form, widgets


class RegisterForm(Form):
    username = forms.CharField(max_length=250,
                               min_length=4)

    first_name = forms.CharField(max_length=250,
                                 min_length=4)

    last_name = forms.CharField(max_length=250,
                                min_length=4)

    email = forms.CharField(max_length=250,
                            min_length=4)

    password_1 = forms.CharField(max_length=250,
                                 min_length=4,
                                 widget=widgets.PasswordInput)

    password_2 = forms.CharField(max_length=250,
                                 min_length=4,
                                 widget=widgets.PasswordInput)

    def clean_username(self):
        if not self.cleaned_data['username'].isalnum():
            self.add_error('username', 'Un nom d\'utilisateur devrait uniquement contenir des caractères '
                                       'alphanumériques')
            return None
        return self.cleaned_data['username']

    def clean(self):
        if self.cleaned_data.get('password_1') != self.cleaned_data.get('password_2'):
            self.add_error('password_1', 'Les mots de passes ne sont pas identiques.')
        return super().clean()
