from __future__ import unicode_literals
from django.db import models

# armorTypes = ["Light", "Medium", "Heavy"]


class DateTimeModel(models.Model):
    """ Handles created at and updated at fields """
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Armor(DateTimeModel):
    """ Protective clothing i.e. Platemail """

    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=100)
    # i.e. Platemail
    price = models.CharField(max_length=100)
    # suggested base price of this item
    armorClass = models.CharField(max_length=100)
    # how protective the armor is
    armorType = models.CharField(max_length=100)
    # Light, Medium, or Heavy
    weight = models.CharField(max_length=100)
    # how heavy the armor is
    stealth = models.CharField(max_length=100)
    # (dis)advantages to being sneaky
    about = models.CharField(max_length=200)
    # About is a description of the the Armor
    # stats, str, dex, wis, may require Many to Many field and new model
