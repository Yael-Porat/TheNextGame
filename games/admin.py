from django.contrib import admin

from .models import *

admin.site.register(Category)

class GameImageInline(admin.TabularInline):
    model = GameImage
    extra = 1

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [GameImageInline]