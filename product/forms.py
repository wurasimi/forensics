from django import forms
from .models import Post
from .models import Contact

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter your title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder':'Enter your content','row':8,}))
    
    class Meta():
        model = Post
        fields = ('image','title','content','price')
        
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control rounded-0 border-start border-secondary border-3 border-top-0 border-bottom-0 border-end-0','placeholder':'Enter  your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control rounded-0 border-start border-secondary border-3 border-top-0 border-bottom-0 border-end-0', 'placeholder':'Enter your Last name '}))
    gmail = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control rounded-0 border-start border-secondary border-3 border-top-0 border-bottom-0 border-end-0', 'placeholder':'example@.gmail.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control rounded-0 border-start border-secondary border-3 border-top-0 border-bottom-0 border-end-0', 'placeholder':'Enter your address ','row':2,}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control rounded-0 border-start border-secondary border-3 border-top-0 border-bottom-0 border-end-0', 'placeholder':'Enter your phone number','row':8,}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control rounded-0 border-start border-secondary border-3 border-top-0 border-bottom-0 border-end-0', 'placeholder':'Describe your comment','row':8,}))
    
    class Meta():
        model = Contact
        fields = ('first_name','last_name','gmail', 'address','phone_number','comment')