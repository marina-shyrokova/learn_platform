from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name", "address", "phone_number", "last_name", "profile_image")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'name', 'address', 'phone_number', 'profile_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')
        # Remove the help text for the username field
        self.fields['username'].help_text = ''

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser