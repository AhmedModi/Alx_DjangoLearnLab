# Update Book in Database

```python
from bookshelf.models import Book

# Retrieve the book created earlier
book = Book.objects.get(title="1984", author="George Orwell")

# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)  # Output: Nineteen Eighty-Four
