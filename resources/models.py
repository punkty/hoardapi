from __future__ import unicode_literals
from django.db import models

ARMOR_TYPES = (
    ('Light','Light armor'),
    ('Medium', 'Medium armor'),
    ('Heavy', 'Heavy armor'),
)


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
    armorType = models.CharField(choices=ARMOR_TYPES, max_length=100)
    # Light, Medium, or Heavy
    weight = models.CharField(max_length=100)
    # how heavy the armor is
    stealth = models.CharField(max_length=100)
    # (dis)advantages to being sneaky
    about = models.CharField(max_length=200)
    # About is a description of the Armor
    # stats, str, dex, wis, may require Many to Many field and new model

class Weapon(DateTimeModel):
    """
    Instruments for fighting monsters. i.e. Greatsword.
    """
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    damage = models.CharField(max_length=50)
    weight = models.CharField(max_length=100)
    properties = models.CharField(max_length=100)

class MagicProperties(DateTimeModel):
    bane = models.BooleanField(default=False)
    defending = models.BooleanField(default=False)
    flaming = models.BooleanField(default=False)
    frost = models.BooleanField(default=False)
    electric = models.BooleanField(default=False)
    spell_storing = models.BooleanField(default=False)
    elemental_burst = models.BooleanField(default=False)
    elemental = models.BooleanField(default=False)
    unholy = models.BooleanField(default=False)
    holy = models.BooleanField(default=False)
    speed = models.BooleanField(default=False)
    wounding = models.BooleanField(default=False)

    
