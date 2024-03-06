from django import forms
def check_size(value):
  if len(value) < 6:
    raise forms.ValidationError("the Password is too short")

class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name' )
    last_name = forms.CharField()
    email = forms.EmailField(help_text = 'write your email', )
    Address = forms.CharField(required = False, )
    Technology = forms.CharField(initial = 'Django', disabled = True, )
    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput, validators = [check_size, ])
    re_password = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)

# , validators = [validators.MinLengthValidator(6)]

# BooleanField
# CharField
# ChoiceField
# DateField
# DecimalField
# EmailField
# FileField, etc.