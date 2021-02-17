from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('title', 'score', 'company')

# Register your models here.
