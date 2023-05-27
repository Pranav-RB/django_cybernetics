from django.contrib import admin
from .models import Event, EventRegistration
# Register your models here.
admin.site.register(Event)
class EventRegistrationAdmin(admin.ModelAdmin):
    readonly_fields = ('event_registration_date', 'event_registration_time')

admin.site.register(EventRegistration, EventRegistrationAdmin)