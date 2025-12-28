from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customeruser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customeruser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        swappable = 'AUTH_USER_MODEL'
