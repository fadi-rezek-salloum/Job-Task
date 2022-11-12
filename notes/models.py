from django.db import models

from accounts.models import Author

class Note(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    