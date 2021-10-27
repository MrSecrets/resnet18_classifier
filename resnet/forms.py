from django import forms
from .models import ImageUpload

class ImageForm(forms.ModelForm):
    image_file=forms.ImageField(widget=forms.FileInput(attrs={"id" :"image"}))

    class Meta:
        model=ImageUpload
        fields= [
        'image_file',
        ]
