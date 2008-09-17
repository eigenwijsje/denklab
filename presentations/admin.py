from django.contrib import admin

from models import Presentation, Resource

class ResourceInline(admin.TabularInline):
    model = Resource

class PresentationAdmin(admin.ModelAdmin):
    inlines = [ResourceInline]
    list_display = ('name', 'title', 'subtitle', 'presented')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('title', 'subtitle', 'notes')

admin.site.register(Presentation, PresentationAdmin)
