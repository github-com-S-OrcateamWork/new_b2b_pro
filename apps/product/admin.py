from django.contrib import admin
from .models import Company, Category, Product, ProductRating, CompanyProduct, SubCategory,ProductImage , Application, Question
from parler.admin import TranslatableAdmin

@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['name','product', 'star', 'review_date', 'email']
    list_filter = ['star']
    search_fields = ['product__name', 'email']
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('name','product', 'star', 'review_comment', 'review_date', 'email'),
        }),
    )
    readonly_fields = ['review_date']

@admin.register(CompanyProduct)
class CompanyProductAdmin(admin.ModelAdmin):
    list_display = ['company', 'product']
    search_fields = ['company__name', 'product__name']


class CategoryAdmin(TranslatableAdmin):
    list_display = ['name']
    list_display_links = ['name',]
    search_fields = ['name']
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('name', 'image'),
        }),
    )

admin.site.register(Category, CategoryAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(TranslatableAdmin):
    inlines = [ProductImageInline]
    list_display = ['name', 'created_at', 'is_featured', 'company']
    list_display_links = ['name']
    search_fields = ['name', 'compound', 'tag']
    list_per_page = 20
    list_filter = ['is_featured', 'category']
    list_editable = ['is_featured']

    fieldsets = (
        (None, {
            'fields': ('name', 'compound','description', 'tag', 'company', 'category', 'is_featured', 'created_at', 'updated_at'),
        },),
    )

admin.site.register(Product, ProductAdmin)

from django.utils.html import format_html


class CompanyAdmin(TranslatableAdmin):
    list_display = ['name', 'type_product', 'country', 'created_at']
    list_display_links = ['name']
    search_fields = ['name', 'type_product__name']
    list_per_page = 20

    def view_location_button(self, obj):
        return format_html('<a href="https://maps.google.com/?q={}" target="_blank">View Location</a>', obj.location)
    
    view_location_button.short_description = 'View Location'

    list_display = ['name', 'country', 'type_product', 'created_at', 'view_location_button']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'type_product', 'image', 'country','phone_number','description','location')
        }),
        ('Social Media Links', {
            'fields': ('facebook', 'instagram', 'telegram', 'youtube'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ['created_at']




class SubCategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'category', 'is_active']
    list_display_links = ['name']
    search_fields = ['name', 'category__name']
    list_filter = ['category', 'is_active']
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'is_active'),
        }),
    )

admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Company, CompanyAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'display_checked', 'date']
    list_filter = ['checked']
    search_fields = ['name', 'phone_number']
    list_per_page = 50
    readonly_fields = ['date']

    def display_checked(self, obj):
        if obj.checked:
            return format_html('<span style="color: green;"><b>&#10004;</b></span>')  # Checked icon
        else:
            return format_html('<span style="color: red;"><b>&#10008;</b></span>')  # X icon

    display_checked.short_description = 'Checked'


admin.site.register(Application, ApplicationAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'display_checked', 'date']
    list_filter = ['checked']
    search_fields = ['name', 'phone_number', 'campany_name']
    list_per_page = 50
    readonly_fields = ['date']

    def display_checked(self, obj):
        if obj.checked:
            return format_html('<span style="color: green;"><b>&#10004;</b></span>')  # Checked icon
        else:
            return format_html('<span style="color: red;"><b>&#10008;</b></span>')  # X icon

    display_checked.short_description = 'Checked'


admin.site.register(Question, QuestionAdmin)
























