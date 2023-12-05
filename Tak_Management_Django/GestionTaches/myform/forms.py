from django import forms
from django.forms import ModelForm, Textarea

# class ContactForm2(forms.Form): 
# 	name = forms.CharField(max_length=200) 
# 	firstname = forms.CharField(max_length=200) 
# 	email = forms.EmailField(max_length=200) 
# 	message = forms.CharField(max_length=1000)


class ContactForm2(forms.Form): 
	name = forms.CharField(max_length=200,initial="votre nom",label="nom") 
	firstname = forms.CharField(max_length=200,initial="votre prenom",label="prenom") 
	email = forms.EmailField(max_length=200,label="mel") 
	message = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))

