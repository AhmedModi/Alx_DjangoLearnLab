# Retrieve Book from Database

```python
from bookshelf.models import Book

# Retrieve the book created earlier
book = Book.objects.get(title="1984", author="George Orwell")

print(book.title)   # Output: 1984
print(book.author)  # Output: George Orwell
