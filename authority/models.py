from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from authority.managers import UserManager


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'

    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
    )


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователя. Заменяет стандартного пользователя Django
    """

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    username = models.CharField(
        max_length=50,
        verbose_name='Имя пользователя',
        help_text='Введите имя пользователя',
        unique=True,
    )
    first_name = models.CharField(
        max_length=75,
        verbose_name='Имя пользователя',
        help_text='Введите имя пользователя',
        blank=True,
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия пользователя',
        help_text='Введите фамилию пользователя',
        blank=True,
    )
    email = models.EmailField(
        blank=True,
    )
    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name='Роль пользователя',
        help_text='Выберите роль пользователя',
    )
    is_active = models.BooleanField(
        verbose_name='Аккаунт активен?',
        help_text='Укажите, активен ли аккаунт',
        blank=True,
    )

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
