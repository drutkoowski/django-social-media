from django import forms
from .models import MessageModel


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Enter username"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class MessageForm(forms.ModelForm):
    body = forms.CharField(label='', max_length=1000)
    image = forms.ImageField(required=False)

    class Meta:
        model = MessageModel
        fields = ['body', 'image']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields["body"].widget.attrs["placeholder"] = "Your message"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'