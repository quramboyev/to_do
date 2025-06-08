from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

User = get_user_model()

class ToDoModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=100, null=False, blank=False, db_column='title'),
        description = RichTextField(_('description'), db_column='description'),
        price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, default=0.00, db_column='price'),
        is_active = models.BooleanField(_('is_active'), default=False, db_column='active'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', blank=True, null=True, db_column='user')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created')
    updated_at = models.DateTimeField( auto_now=True, db_column='updated')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'
        db_table = 'todo'


class FakeModel(models.Model):
    email = models.EmailField(_('email'), db_column='gmail')
    text = models.TextField(_('text'), db_column='text')
    img = models.ImageField(_('img'), upload_to='fake/', blank=True, null=True, db_column='image')

    class Meta:
        verbose_name = 'Fake'
        verbose_name_plural = 'Fake`s'
        db_table = 'Fake'
