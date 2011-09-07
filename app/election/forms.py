from django import forms
from election.models import Election
from django.utils.translation import ugettext_lazy as _

class ElectionAdminForm(forms.ModelForm):
	class Meta:
		model = Election
