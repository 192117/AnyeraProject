from django.core.validators import MinValueValidator
from django.db import models

from authority.models import User


class Animals(models.Model):

    name = models.CharField(
        verbose_name='Кличка питомца',
        max_length=100,
    )
    age = models.IntegerField(
        verbose_name='Возраст питомца',
        validators=[
            MinValueValidator(1),
        ],
    )
    kind_of_animal = models.CharField(
        verbose_name='Вид питомца',
        max_length=255,
    )
    photo = models.ImageField(
        verbose_name='Фото питомца',
        upload_to='animals_photo/',
        blank=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='animals',
        verbose_name='Хозяин питомца',
    )

    def __str__(self):
        return f'{self.name} - {self.user.username}'

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
