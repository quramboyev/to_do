from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

User = get_user_model()

class ToDoModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=100, null=False, blank=False),
        description = RichTextField(_('description')),
        price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, default=0.00),
        is_active = models.BooleanField(_('is_active'), default=False),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'


class FakeModel(models.Model):
    email = models.EmailField(_('email'))
    text = models.TextField(_('text'))