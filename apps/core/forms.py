from django import forms
from apps.core.models import Box, Material, Appointment
from django.core.exceptions import ValidationError



class DataForm_v1(forms.ModelForm):
    """Basic solution"""
    get_box = forms.CharField(max_length=24, required=True)
    get_material = forms.CharField(max_length=150, required=True)
    class Meta:
        model = Appointment
        exclude = ["box", "material"]

class DataForm_v2(forms.ModelForm):
    """Advanced solution"""
    box = forms.CharField(max_length=24, required=True)
    material = forms.CharField(max_length=24, required=True)

    class Meta:
        model = Appointment
        fields = ["box", "material"]

    def __init__(self, *args, **kwargs) -> None:
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.created_by = self.user
        return super().save(*args, **kwargs)

    def clean_material(self):
        material = Material.objects.filter(code=self.cleaned_data["material"]).first()
        if material is None:
            raise ValidationError("Invalid Material")

        return material

    def clean_box(self):
        box = Box.objects.filter(code=self.cleaned_data["box"]).first()
        if box is None:
            raise ValidationError("Invalid Box")

        return box
