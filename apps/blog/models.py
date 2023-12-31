
from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.utils.text import slugify


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name')),
    )
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'))

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
            # super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Post(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=300, verbose_name=_('Sarlavha')),
        description = models.CharField(max_length=1000, verbose_name=_('Maqola haqida qisqacha')),
        content = models.TextField(verbose_name=_('Maqola')),
    )
    categories = models.ManyToManyField(Category, verbose_name=_('Kategoriyalar'))
    image = models.ImageField(upload_to='post_images', verbose_name=_('Rasm'))
    created_at = models.DateTimeField(verbose_name=_('Created at'))
    updated_at = models.DateTimeField(verbose_name=_('Updated at'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Maxus post'))
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'))
    views = models.IntegerField(default=0, verbose_name=_('Ko\'rilganlar soni'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Maqola')
        verbose_name_plural = _('Maqolalar')
        ordering = ['-created_at']
