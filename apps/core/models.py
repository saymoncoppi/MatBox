from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Material(models.Model):
    code = models.CharField(
        max_length=150, blank=True, null=True, verbose_name=_("Code")
    )
    description = models.CharField(max_length=150, verbose_name=_("Description"))

    def __str__(self):
        return self.code


class Box(models.Model):
    is_empty = models.BooleanField(default=True, verbose_name=_("Empty"))
    code = models.CharField(
        max_length=150, blank=True, null=True, verbose_name=_("Code")
    )
    description = models.CharField(max_length=150, verbose_name=_("Description"))

    def __str__(self):
        return self.code


class Appointment(models.Model):
    box = models.ForeignKey(
        Box,
        related_name="from_box",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name=_("Box"),
    )
    material = models.ForeignKey(
        Material,
        related_name="from_material",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name=_("Material"),
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        editable=False,
        null=True,
        blank=True,
        verbose_name=_("Created by"),
    )
    created = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name=_("Created")
    )

    def __str__(self):
        return f"{self.box} - {self.material}"

    def created_updated(model, request):
        # obj = model.objects.latest('pk')
        obj = model
        if (obj.created_by is None) or (obj.created_by == ""):
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "box",
        "material",
        "created",
        "created_by",
    )
    readonly_fields = (
        "created",
        "created_by",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "box",
                    "material",
                )
            },
        ),
        (
            "Logs",
            {
                "classes": ("collapse",),
                "fields": (
                    "created",
                    "created_by",
                ),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        # Passar request como argumento.
        obj.created_updated(request)
        super().save_model(request, obj, form, change)
