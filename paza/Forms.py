from Sikika.models import NewPost
from django import forms
from cloudinary.models import CloudinaryField

class PostForm(forms.Form):
    image = forms.ImageField()
    image_name = forms.CharField()
    image_caption = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = NewPost
        fields = ['image']

class CommentForm(forms.Form):
    body = forms.CharField(widget = forms.TextInput(attrs = {"class": "form-control", "placeholder": "Leavea Comment"}))