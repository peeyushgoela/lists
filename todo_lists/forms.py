from django import forms

priority_choices=((0, 'High'),(1,'Medium'),(2,'Low'))

class signup_form(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()

class login_form(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class addtask_form(forms.Form):
    item=forms.CharField()
    priority=forms.ChoiceField(widget=forms.Select, choices=priority_choices)

class edittask_form(forms.Form):
    item=forms.CharField()
    priority=forms.ChoiceField(widget=forms.Select, choices=priority_choices)
    is_complete=forms.BooleanField(required=False)

    
