from django import forms
from apps.core.models import Box, Material, Appointment


class DataForm(forms.ModelForm):
    get_box = forms.CharField(max_length=24, required=True)

    get_material = forms.CharField(max_length=150, required=True)

    box = forms.ModelChoiceField(
        required=False,
        queryset=Box.objects.filter(code=get_box),
        widget=forms.HiddenInput(),
    )
    material = forms.ModelChoiceField(
        required=False,
        queryset=Material.objects.filter(code=get_material),
        widget=forms.HiddenInput(),
    )

    print(material, box)

    class Meta:
        model = Appointment
        fields = ["box", "material"]
