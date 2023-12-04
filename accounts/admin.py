from django.contrib import admin
from accounts.models import Patient,Doctor,Secretary

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Secretary)
