from django.contrib import admin

from models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    list_display = ('title', 'published', 'last_updated')
    list_filter = ('categories',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'intro', 'body')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
