from __future__ import unicode_literals
from django.db import models
from datetime import datetime


ARMOR_TYPES = (
    ('Light','Light armor'),
    ('Medium', 'Medium armor'),
    ('Heavy', 'Heavy armor'),
)

class DateTimeModel(models.Model):
    """
    Handles created and updated fields
    """
    class Meta:
        abstract = True

    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)

class Armor(DateTimeModel):
    """ Protective clothing i.e. Platemail """

    def __unicode__(self):
        return self.name

    # i.e. Platemail
    name = models.CharField(max_length=100)

    # how much gold silver and or copper pices it would trade for. i.e. 3gp 10sp 3cp
    price = models.CharField(max_length=100)

    # how protective the armor is
    armorClass = models.CharField(max_length=100)

    # Light, Medium, or Heavy
    armorType = models.CharField(choices=ARMOR_TYPES, max_length=100)

    # how heavy the armor is
    weight = models.CharField(max_length=100)

    # (dis)advantages to being sneaky
    stealth = models.CharField(max_length=100)

    # About is a description of the Armor
    about = models.CharField(max_length=200)

    # set to True if armor contains magical properties
    magical = models.BooleanField(default=False)

    # stats, str, dex, wis, may require Many to Many field and new model


class ArmorStats(DateTimeModel):
    """
    Stat bonuses that accompany a piece of armor.
    """
    charisma = models.IntegerField(default=0, blank=True)
    constitution = models.IntegerField(default=0, blank=True)
    defense = models.IntegerField(default=0, blank=True)
    dexterity = models.IntegerField(default=0, blank=True)
    luck = models.IntegerField(default=0, blank=True)
    perception = models.IntegerField(default=0, blank=True)
    strength = models.IntegerField(default=0, blank=True)
    willpower = models.IntegerField(default=0, blank=True)
    wisdom = models.IntegerField(default=0, blank=True)
    armor = models.ForeignKey(Armor, related_name='stats', on_delete=models.CASCADE)