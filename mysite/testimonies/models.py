from django.db import models

# Create your models here.
class Testimonials(models.Model):
    """adding a testimonial"""

    name = models.CharField(max_length=100)
    testimonial = models.TextField(default="")

    def __str__(self):
        return self.testimonial[:50]