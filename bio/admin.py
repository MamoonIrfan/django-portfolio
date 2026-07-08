from django.contrib import admin

from .models import Bio, Achievement, ContactMessage


admin.site.register(Bio)
admin.site.register(Achievement)
admin.site.register(ContactMessage)