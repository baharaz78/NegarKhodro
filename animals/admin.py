from django.contrib.admin import register
from animals.models import Animal
from django.contrib import admin


@register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species')
    list_filter = ('species',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': (
                ('created_at', 'updated_at'),
                'species',
                'name',
            ),
        }),
    )
