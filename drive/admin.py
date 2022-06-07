from django.contrib import admin
from drive.models import drivetest

# Register your models here.

@admin.register(drivetest)
class  driveAdmin(admin.ModelAdmin):


    list_display =('pk', 'name','csv', 'kml', 'bill')

    # list_display_links = ('pk')

    list_editable=('name','csv', 'kml', 'bill')
