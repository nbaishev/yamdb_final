from django.contrib import admin

from .models import Category, Genre


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year',
                    'category',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )
    search_fields = ('name',)
    list_filter = ('name', 'slug',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )

    search_fields = ('name',)
    list_filter = ('name', 'slug',)
