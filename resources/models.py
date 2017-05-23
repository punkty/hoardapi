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
    type = models.CharField(choices=ARMOR_TYPES, max_length=100)

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
    intelligence = models.IntegerField(default=0, blank=True)
    luck = models.IntegerField(default=0, blank=True)
    perception = models.IntegerField(default=0, blank=True)
    strength = models.IntegerField(default=0, blank=True)
    wisdom = models.IntegerField(default=0, blank=True)
    armor = models.ForeignKey(Armor, related_name='stats', on_delete=models.CASCADE)


class Mount(DateTimeModel):
    """
    Vehicles or animals that aid in travel and carrying.
    """
    name = models.CharField(max_length=100)

    nickname = models.CharField(max_length=100)

    MOUNT_TYPES = (
        ('Biological','Bio'),
        ('Mechanical', 'Mech'),
        ('Summoned', 'Summon'),
    )

    type = models.CharField(choices=MOUNT_TYPES, max_length=100)

    # how fast does it travel
    speed = models.CharField(max_length=50)

    # maximum carrying capacity in weight
    max_burden = models.CharField(max_length=50)

    price = models.CharField(max_length=100)

    # the amount of damage the mount can sustain before dying or breaking
    health = models.CharField(max_length=100)

    description = models.CharField(max_length=200)


class Potion(DateTimeModel):
    """
    A small ornament or item, usually mundane and of little value
    """

    # i.e. Light Potion of Healing
    name = models.CharField(max_length=100)

    # i.e. regains some health
    effect = models.CharField(max_length=200)

    side_effect = models.CharField(max_length=200, default="None", blank=True)


class Tool(DateTimeModel):
    """
    Instruments used for aiding in a craft or repair.
    """

    name = models.CharField(max_length=100)

    description = models.CharField(max_length=200)


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

class MagicalProperty(DateTimeModel):
    """
    i.e. Flaming. An item with this property would appear to be on fire.
    """
    name = models.CharField(max_length=100)

    description = models.CharField(max_length=200)


class Weapon(DateTimeModel):
    """ i.e. Longsword """

    # i.e. Longsword
    name = models.CharField(max_length=100)

    price = models.CharField(max_length=100)

    # format XdY where  (the x amount of)d(with y many sides) 1d20
    damage = models.CharField(max_length=100)

    range = models.CharField(max_length=25)

    WEAPON_TYPES = (
    ('Simple M','Simple Melee'),
    ('Simple R', 'Simple Ranged'),
    ('Martial M', 'Martial Melee'),
    ('Martial R', 'Martial Ranged'),
    )
    # Light, Medium, or Heavy
    type = models.CharField(choices=WEAPON_TYPES, max_length=100)

    # how heavy the weapon is
    weight = models.CharField(max_length=100)

    # (dis)advantages to being sneaky
    stealth = models.CharField(max_length=100, default="-", blank=True)

    # About is a description of the Armor
    description = models.CharField(max_length=200)

    # set to True if armor contains magical properties
    magical = models.BooleanField(default=False)

    magical_properties = models.ManyToManyField(MagicalProperty, blank=True)

class WeaponStats(DateTimeModel):
    """
    Stat bonuses that accompany a weapon.
    """
    charisma = models.IntegerField(default=0, blank=True)
    constitution = models.IntegerField(default=0, blank=True)
    defense = models.IntegerField(default=0, blank=True)
    dexterity = models.IntegerField(default=0, blank=True)
    intelligence = models.IntegerField(default=0, blank=True)
    luck = models.IntegerField(default=0, blank=True)
    perception = models.IntegerField(default=0, blank=True)
    strength = models.IntegerField(default=0, blank=True)
    wisdom = models.IntegerField(default=0, blank=True)
    weapon = models.ForeignKey(Weapon, related_name='stats', on_delete=models.CASCADE)
