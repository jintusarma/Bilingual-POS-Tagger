from django.contrib import admin
from .models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user","is_verified"]

class VerifierAdmin(admin.ModelAdmin):
    list_display = ["verifier","verifier_type"]


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Verifier,VerifierAdmin)