from django import forms
from django.forms import fields, widgets
from .models import Post,Category

# choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class': "form-control"}),
            
            'title_tag' : forms.TextInput(attrs={'class': "form-control"}),
            # 'author' : forms.Select(attrs={'class': "form-control"}),
            'author' : forms.TextInput(attrs={'class': "form-control",'value':"",'id':"elder",'type':"hidden"}),
            'category':forms.Select(choices=choice_list, attrs={'class': "form-control"}),
            'body' : forms.Textarea(attrs={'class': "form-control"}),
             'snippet' : forms.Textarea(attrs={'class': "form-control"}),
        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class': "form-control"}),
            'title_tag' : forms.TextInput(attrs={'class': "form-control"}),
            # 'author' : forms.Select(attrs={'class': "form-control"}),
            'body' : forms.Textarea(attrs={'class': "form-control"}),
            'snippet' : forms.Textarea(attrs={'class': "form-control"}),
        }