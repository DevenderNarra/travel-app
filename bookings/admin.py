from django.contrib import admin
from .models import Bus, Seat

class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'origin', 'destination', 'start_time', 'reach_time', 'price')
   

admin.site.register(Bus,BusAdmin)
admin.site.register(Seat)