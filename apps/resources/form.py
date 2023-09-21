from django import forms


class PostResourceForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
              attrs={
            'class': 'title-input',
            'placeholder': 'Enter a title'
            }
        )) # input with type = 'text'
    link = forms.URLField() # input with type = 'URL'
    description = forms.CharField(widget=forms.Textarea) # input with type = 'textarea'
    
class PostCategory(forms.Form):
    name = forms.CharField()