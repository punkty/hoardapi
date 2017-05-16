from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class DateTimeModel(models.Model):
    """
    Handles created and updated fields
    """ 
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        abstract = True

class Armor(DateTimeModel):
    """ Protective clothing i.e. Platemail """

    # i.e. Platemail
    name = models.CharField(max_length=100)

    # how much gold silver and or copper pices it would trade for. i.e. 3gp 10sp 3cp
    price = models.CharField(max_length=100)

    # how protective the armor is
    armor_class = models.CharField(max_length=100)

    ARMOR_TYPES = (
    ('Light','Light armor'),
    ('Medium', 'Medium armor'),
    ('Heavy', 'Heavy armor'),
    )
    # Light, Medium, or Heavy
    armor_type = models.CharField(choices=ARMOR_TYPES, max_length=100)

    # how heavy the armor is
    weight = models.CharField(max_length=100)

    # (dis)advantages to being sneaky
    stealth = models.CharField(max_length=100)

    # About is a description of the Armor
    description = models.CharField(max_length=200)

    # set to True if armor contains magical properties
    magical = models.BooleanField(default=False)


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

class Potion(DateTimeModel):
    """ 
    A small ornament or item, usually mundane and of little value
    """
    
    # i.e. Light Potion of Healing
    name = models.CharField(max_length=100)

    # i.e. regains some health
    effect = models.CharField(max_length=200)

    side_effect = models.CharField(max_length=200, default="None", blank=True)

class Trinket(DateTimeModel):
    """ 
    A small ornament or item, usually mundane and of little value
    """

    # i.e. A rabbits foot
    name = models.CharField(max_length=100)

    # a description of what this trinket is
    description = models.CharField(max_length=200)

    # set to True if armor contains magical properties
    magical = models.BooleanField(default=False)

    # if it is magical what does it do
    effects = models.CharField(max_length=200, blank=True, default="-")
