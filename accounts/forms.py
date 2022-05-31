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
