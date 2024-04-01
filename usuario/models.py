from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from uploader.models import Image


class Usuario(AbstractUser):
    class TipoUsuario(models.IntegerChoices):
        CLIENTE = 1, "Cliente"
        VENDEDOR = 2, "Vendedor"
        GERENTE = 3, "Gerente"
    username = models.CharField(max_length=50, unique=True, default="...")
    email = models.EmailField(_("e-mail address"), unique=True)
    tipo_usuario = models.IntegerField(_("User Type"), choices=TipoUsuario.choices, default=TipoUsuario.CLIENTE)
    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
