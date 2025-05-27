from django import forms
from django.utils.translation import gettext_lazy as _
from .models import NameRegistration

class NameRegistrationForm(forms.ModelForm):
    accept_terms = forms.BooleanField(
        label=_('Akceptuję regulamin'),
        required=True
    )

    class Meta:
        model = NameRegistration
        fields = ['name', 'country', 'postal_code']
        labels = {
            'name': _('Nazwa'),
            'country': _('Kraj/Państwo'),
            'postal_code': _('Kod pocztowy'),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned = super().clean()
        # administratorom pozwalamy na nieograniczoną liczbę wpisów
        if not self.user.is_staff:
            # zwykły użytkownik – maksymalnie 5 wpisów
            count = NameRegistration.objects.filter(user=self.user).count()
            if count >= 5:
                raise forms.ValidationError(
                    _('Możesz zarejestrować maksymalnie 5 nazw.')
                )
        return cleaned

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.user
        obj.status = 'reserved'
        if commit:
            obj.save()
        return obj
