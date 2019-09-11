from django.db import models
from api.models import User
from django.utils.translation import ugettext_lazy as _


class Guest(User):
    phone_number = models.CharField(_('phone number'),max_length=20,unique=True)
    occupation = models.CharField(_('occupation'), null=True,max_length=100)
    address = models.CharField(_('address(town)'), null=True,max_length=100)
    country = models.CharField(_('address(town)'),max_length=100)
    work_place = models.CharField(_('work place'), null=True,max_length=100)

    def __str__(self):
        return "{}".format(self.phone_number)
