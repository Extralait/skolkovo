import os

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    """
    Менеджер пользователя (Модель)
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        База создания пользователя
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Создание пользователя
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Создание суперпользователя
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Custom User Class
class User(AbstractUser):
    """
    Пользователь (Модель)
    """
    username = None
    email = models.EmailField('Email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


class EmailMessage(models.Model):
    class StatusType(models.TextChoices):
        """
        Тип blockchain
        """
        MALEVOLENT = 'malevolent', 'Malevolent'
        SAFE = 'safe', 'Safe'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_email = models.EmailField('From user')
    to_email = models.EmailField('To user')
    date = models.DateTimeField('Date and time of sending')
    content_type = models.CharField('Content type', max_length=100)
    x_uid = models.CharField('X-UID', max_length=200)
    body = models.TextField('Body')
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        verbose_name='Status',
        max_length=20,
        choices=StatusType.choices,
        null=True,
        blank=True
    )
    accuracy = models.PositiveIntegerField('Accuracy', null=True, blank=True)

    class Meta:
        verbose_name = 'Email message'
        verbose_name_plural = 'Email messages'

    def __str__(self):
        return self.from_email + ' - ' + self.to_email
