from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from blood.models import User
from blood import views as v


UserModel = get_user_model()


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'email_duplicate': _('This email address is already in use'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        # help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        # help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = UserModel
        fields = ('email', 'full_name', 'blood_type', 'date_birth', 'gender', 'avatar')
        field_classes = { 'email': UsernameField }
        widgets = {
        'date_birth': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True
        
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-control'

    # Check if e-mail has already been used
    def clean_email(self):
        email = self.cleaned_data.get('email')

        users = User.objects.all()
        for user in users:
            e = v.decrypt(email=user.email).get('email')
            print(e)

            if email.casefold() == e.casefold():
                raise forms.ValidationError(self.error_messages['email_duplicate'], code='email_duplicate')
            else:
                return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user