from django.contrib import admin

from .models import User, GuideProfile
from .utils import create_profile


# Register your models here.
@admin.register(User)
class CustomAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        create_profile(form)
        super().save_model(request, obj, form, change)


@admin.register(GuideProfile)
class GuideProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'verification_status')
    list_display_links = ['id']
    list_filter = ('user', 'verification_status', 'current_location')
    search_fields = ('id', 'user', 'verification_status')
    list_editable = ['verification_status']

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

