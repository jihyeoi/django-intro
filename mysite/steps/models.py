from django.db import models


class Step(models.Model):
    """step for how to create a django app"""

    # if i do not explicitly define a primary key,
    # django adds an integerfield to my model as the primary key

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Direction(models.Model):
    """adding a direction to a step"""

    direction_text = models.TextField(default="")
    step = models.ForeignKey(Step, related_name='directions', on_delete=models.CASCADE)

    def __str__(self):
        return self.direction_text[:50]  # Return first 50 characters







