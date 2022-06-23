from django.contrib import admin
from .models import Car, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_repaired', 'is_finished')
    list_filter = ('is_repaired', 'is_finished')
    search_fields = ('name',)
    list_editable = ('is_repaired', 'is_finished')
    actions = ['enable_is_finished', 'disable_is_finished',
               'enable_is_repaired', 'disable_is_repaired']

    def enable_is_finished(modeladmin, request, queryset):
        for elm in queryset:
            print(elm)
            elm.is_finished = True
            elm.save()

    def disable_is_finished(modeladmin, request, queryset):
        for elm in queryset:
            elm.is_finished = False
            elm.save()

    def enable_is_repaired(modeladmin, request, queryset):
        for elm in queryset:
            elm.is_repaired = True
            elm.save()

    def disable_is_repaired(modeladmin, request, queryset):
        for elm in queryset:
            elm.is_repaired = False
            elm.save()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ['email', "role"]
    fieldsets = (
        (None, {"fields": ("email", "password","role")}),
        
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser")}
        ),
        ("Important dates", {"fields": ("last_login",)})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide", ),
            "fields": ("email", "password1", "password2","role")
        }),
    )


