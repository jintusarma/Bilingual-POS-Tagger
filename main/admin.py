from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Dataset)
admin.site.register(TaggerDetails)
admin.site.register(VerfierDetails)
admin.site.register(MetaData)