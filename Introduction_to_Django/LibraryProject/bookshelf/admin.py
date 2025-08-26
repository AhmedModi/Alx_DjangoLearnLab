from django.contrib import admin
from .models import Book

# Customize how Book appears in the admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns displayed in the list view
    list_display = ("title", "author", "publication_year")

    # Add filtering options on the right sidebar
    list_filter = ("publication_year", "author")

    # Enable search functionality
    search_fields = ("title", "author")
