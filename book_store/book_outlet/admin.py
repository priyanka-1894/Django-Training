from django.contrib import admin

from .models import Address, Book, Author, Country

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "rating", "author",)
    list_display = ("title", "rating", "author", "is_bestselling")

class AuthorAdmin(admin.ModelAdmin):    
    list_display = ("first_name", "last_name")
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "postal_code", "city")

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)