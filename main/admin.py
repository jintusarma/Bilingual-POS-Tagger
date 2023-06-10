from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(BodoDataset)
admin.site.register(AssameseDataset)
# admin.site.register(TaggerDetails)
# admin.site.register(VerfierDetails)
admin.site.register(MetaData)
admin.site.register(Tagset)