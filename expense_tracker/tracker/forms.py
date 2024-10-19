from django import forms
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    phone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter current password'}), required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'}), required=False)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone','profile_image']

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get("current_password")
        new_password = cleaned_data.get("new_password")

        # Add your password validation logic here
        # For example, check if the current password is correct
        # and set the new password if provided

        return cleaned_data
