from django.core.validators import MinValueValidator
from django.db import models

class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'


