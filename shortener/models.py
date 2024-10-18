from django.db import models
import random
import string

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, default=generate_short_url)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.short_url