from django.contrib import admin

from .models import Category, Recipe

# @admin.register()
# admin.site.register()


class CategoryAdmin(admin.ModelAdmin):
          ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
        ...

admin.site.register(Category, CategoryAdmin)