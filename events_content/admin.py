from django.contrib import admin
from .models import EventPage

class EventPageAdmin(admin.ModelAdmin):
    list_display = [
        "name",

    ]
    search_fields = ("name","name_slug")
    class Meta:
        model = EventPage


admin.site.register(EventPage,EventPageAdmin)
