from django import forms
from election.models import Election, Question
from django.utils.translation import ugettext_lazy as _

class ElectionAdminForm(forms.ModelForm):
	class Meta:
		model = Election

class QuestionAdminForm(forms.ModelForm):
	class Meta:
		model = Question
