from django.contrib import admin
from goods.models import Categories, Products

# Регистрация модели Categories в админ-панели Django
# admin.site.register(Categories)
# admin.site.register(Products)

# Создание админ-класса для модели Categories
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое заполнение slug на основе name

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое заполнение slug на основе name
