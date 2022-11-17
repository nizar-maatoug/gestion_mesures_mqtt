
from django.forms import ModelForm, TextInput,DateTimeInput
from .models import Mesure


class MesureForm(ModelForm):
    class Meta:
        model=Mesure
        fields='__all__'
        widgets={
            'valeur':TextInput(attrs={"type":"number"}),
            'datePrise': DateTimeInput( attrs={"type": "datetime-local"}),
        }
