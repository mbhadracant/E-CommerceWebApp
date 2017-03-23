from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'street_address',
            'city',
            'post_code',
            'country',

        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.street_address = self.cleaned_data['street_address']
        user.city = self.cleaned_data['city']
        user.post_code = self.cleaned_data['post_code']
        user.country = self.cleaned_data['country']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'street_address',
            'city',
            'post_code',
            'country',
        )
