from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from BackEnd.Apps.Auth.models import CustomUser
from BackEnd.Apps.Recipes.Utils.utils import Validators


class Medicamento(models.Model):
  STATUS_CHOICES = (
    ('activo', 'Activo'),
    ('baja', 'De Baja'),
  )

  code = models.CharField(_('Código'),
                          max_length=13,
                          unique=True,
                          validators=[Validators.validate_code]
                          )
  description = models.CharField(_('Nombre'),
                                 max_length=255,
                                 unique=True,
                                 validators=[Validators.validate_description]
                                 )
  price = models.DecimalField(_('Precio'),
                              max_digits=10,
                              decimal_places=2,
                              validators=[Validators.validate_price, MinValueValidator(0.01)]
                              )
  stock = models.CharField(_('Stock'),
                           max_length=10,
                           null=False,
                           blank=False,
                           validators=[Validators.validate_stock]
                           )
  status = models.CharField(_('Estado'),
                            max_length=10,
                            choices=STATUS_CHOICES,
                            default='active'
                            )
  user = models.ForeignKey(CustomUser, verbose_name=_('Usuario'), on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.descripcion} - {self.codigo} -'
