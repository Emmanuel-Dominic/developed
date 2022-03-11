from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password
from .widgets import PlaceholderInput, ShowHidePasswordWidget
from .models import User, Profile


# create your forms here.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        error_messages = {
            'username': {
                'unique': _('Please username is taken, enter another.')
            }
        }
        widgets = {
            'username': PlaceholderInput, # forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': ShowHidePasswordWidget # forms.PasswordInput
        }

    def save(self, commit=True, *args, **kwargs):
        # m = super(UserForm, self).save(commit=False) # python2
        m = super().save(commit=False) # python3
        m.password = make_password(self.cleaned_data.get('password'))
        m.email = self.cleaned_data.get('email').lower()
        m.username = self.cleaned_data.get('username').lower()
        if commit:
            m.save()
        return m

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'bio', 'phone', 'zipcode',  'address']
    
    # def clean(self):
    #     address = self.cleaned_data.get('address')
    #     zipcode = self.cleaned_data.get('zipcode')
    #     if address and zipcode:
    #         if zipcode > '1234':
    #             msg = 'we donot deliver in the area'
    #             self.add_error('address', msg)
    #             self.add_error('zipcode', msg)
    #             raise ValidationError('There is a probem with the zipcode entered')

    # def clean_zipcode(self):
    #     zipcode = self.cleaned_data.get('zipcode')
    #     if(len(zipcode)!=4):
    #         raise forms.ValidationError('zipcode must be of length 4')
    #     return zipcode