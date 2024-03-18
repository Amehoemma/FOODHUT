from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.BookTable)
class booktableadmin(admin.ModelAdmin):
    list_display=['email','number_guest','time','date']