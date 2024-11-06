from django.contrib import admin
from .models import User, Vehicle, Suspect, Call, Dispatcher, Fire, Citation, Arrest

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('badge', 'last_name', 'email')  # Changed 'name' to 'last_name'
    search_fields = ('badge', 'last_name', 'email')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate', 'make', 'model')
    search_fields = ('plate', 'make', 'model')

@admin.register(Suspect)
class SuspectAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'address')
    search_fields = ('name', 'alias')

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('location', 'code', 'created_at')
    search_fields = ('location', 'description')

@admin.register(Dispatcher)
class DispatcherAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'last_name', 'email')
    search_fields = ('user_name', 'last_name', 'email')

@admin.register(Fire)
class FireAdmin(admin.ModelAdmin):
    list_display = ('badge', 'last_name', 'status')
    search_fields = ('badge', 'last_name')

@admin.register(Citation)
class CitationAdmin(admin.ModelAdmin):
    list_display = ('charge', 'location', 'perp')
    search_fields = ('charge', 'location', 'perp__name')

@admin.register(Arrest)
class ArrestAdmin(admin.ModelAdmin):
    list_display = ('reason', 'perp', 'created_at')
    search_fields = ('reason', 'perp__name')

# You can customize the admin site header here if you want
admin.site.site_header = 'Wicked RP Admin Panel'