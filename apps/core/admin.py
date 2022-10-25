from django.contrib import admin

from .models import Material
from .models import Box
from .models import Appointment, AppointmentAdmin


admin.site.register(Material)
admin.site.register(Box)
admin.site.register(Appointment, AppointmentAdmin)
