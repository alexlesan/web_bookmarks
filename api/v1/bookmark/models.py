from django.contrib.auth.models import User
from django.db import models


class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name="bookmarks", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bookmarks'
        ordering = ['created_at']
        verbose_name = "Bookmarks"
        verbose_name_plural = "Bookmarks"

    def __str__(self):
        return self.title