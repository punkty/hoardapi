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


class Weapon(DateTimeModel):
    """
    Instruments for fighting monsters. i.e. Greatsword.
    """
    # Name of the weapon. i.e. Battle Axe, Excalibur, etc.
    name = models.CharField(max_length=100)

    # how much gold silver and or copper pices it would trade for. i.e. 3gp 10sp 3cp
    price = models.CharField(max_length=100)

    # how much damage this weapon inflicts on a successful strike or possibly a range
    damage = models.CharField(max_length=50)

    # how heavy this weapon is
    weight = models.CharField(max_length=100)

class MagicProperty(DateTimeModel):
    """
    The properties that make a particular item 'Magical'
    """
    # name of the magical propery i.e. Flaming, Unholy, Poison, ...
    name = models.CharField(max_length=100)

    # brief description about what this magical property does
    about = models.CharField(max_length=200)

    # a list of weapons that carry this property
    weapons = models.ManyToManyField(Weapon, related_name="magical_properties")

    # a list of armors that carry this property
    armors = models.ManyToManyField(Armor, related_name="magical_properties")
    
class ArmorStats(DateTimeModel):
    """
    Stat bonuses that accompany a piece of armor.
    """
    charisma = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)
    perception = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    willpower = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    armor = models.ForeignKey(Armor, related_name='stats', on_delete=models.CASCADE)