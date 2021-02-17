from django.contrib import admin
from .models import Category, Company

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug')
	list_filter = ('title', 'slug')
	search_fields = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'owner', 'category', 'status', 'average_rating')
	list_filter = ('title', 'owner', 'category', 'status')
	search_fields = ('title', 'description')
	prepopulated_fields = {'slug': ('title',)}

# Register your models here.
