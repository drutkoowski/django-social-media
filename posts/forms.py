from django import forms
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin

from .models import Post, PostComments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('photo', 'description')

    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["photo"].widget.attrs["placeholder"] = "Enter photo"
        self.fields["photo"].widget.attrs["id"] = "post-photo"
        self.fields["photo"].widget.attrs[
            'onchange'] = "document.getElementById('photo').src = window.URL.createObjectURL(this.files[0])"
        self.fields["description"].widget.attrs["placeholder"] = "Enter your caption"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["content"].widget.attrs["placeholder"] = "Enter comment"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
