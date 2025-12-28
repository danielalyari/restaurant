from django.contrib import admin

from . import models

@admin.register(models.FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = list_display


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["name", "old_price", "price"]
    list_display_links = list_display
    filter_horizontal = ["food_types"]


@admin.register(models.SuggestionsCritics)
class suggestionCriticsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "text"]
    list_display_links = list_display


@admin.register(models.Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "amount"]
    list_display_links = list_display
