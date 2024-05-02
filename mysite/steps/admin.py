from django.contrib import admin
from .models import Step, Direction

class DirectionInline(admin.TabularInline):
    model = Direction
    extra = 1  # Number of extra Direction forms

class StepAdmin(admin.ModelAdmin):
    inlines = [DirectionInline]

admin.site.register(Step, StepAdmin)