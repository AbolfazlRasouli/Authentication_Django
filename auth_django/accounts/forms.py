from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'age', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'age', 'email')
