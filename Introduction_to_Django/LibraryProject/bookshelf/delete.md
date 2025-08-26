# Delete Book from Database

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four", author="George Orwell")

# Delete the book
book.delete()

# Confirm deletion
print(Book.objects.filter(title="Nineteen Eighty-Four", author="George Orwell").exists())  # Output: False
