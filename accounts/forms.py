from django import forms
from .models import Account, UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Enter username"
        self.fields["password"].widget.attrs["placeholder"] = "Password"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password')

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "First name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last name"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Phone number"
        self.fields["password"].widget.attrs["placeholder"] = "Password"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'