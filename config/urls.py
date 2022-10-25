from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from apps.core.views import *

urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("appointment_mobile_v1", appointment_mobile_v1, name="appointment_mobile_v1"),
    path("appointment_mobile_v2", appointment_mobile_v2, name="appointment_mobile_v2"),
    path("logout", pagelogout, name="logout"),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
