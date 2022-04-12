from django import forms
from ipl_app.models import Team,Player

class teamform(forms.ModelForm):
	class Meta:
		model=Team
		fields="__all__"
class playerform(forms.ModelForm):
	class Meta:
		model=Player
		fields="__all__"