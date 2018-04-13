from django import forms
from django.contrib.auth import authenticate


class loginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control form-login' , 'placeholder':'Username','autocomplete': 'off'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control form-login ', 'placeholder':' Password','autocomplete': 'off'}))

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


