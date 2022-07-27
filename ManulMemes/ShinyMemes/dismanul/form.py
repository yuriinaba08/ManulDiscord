class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("name", "img")