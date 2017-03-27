from __future__ import unicode_literals
from rest_framework import serializers


from .models import (
    Armor,
    MagicProperty,
    Stats,
    Weapon,
)

class StatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stats
        fields = (
            'id', 
            'charisma',
            'constitution', 
            'defense',
            'dexterity',
            'luck',
            'perception',
            'strength',
            'willpower',
            'wisdom',
            )

class ArmorSerializer(serializers.ModelSerializer):
    stats = StatsSerializer(many=True)

    class Meta:
        model = Armor
        fields = (
                'id', 
                'name', 
                'price', 
                'armorClass', 
                'armorType', 
                'weight', 
                'stealth', 
                'about',
                'magical',
                'stats', 

        )

    def create(self, validated_data):
        """
        Create and return a new Armor, given the validated data.
        """
        armor_stats = validated_data.pop('stats')
        armor = Armor.objects.create(**validated_data)

        for stat in armor_stats:
            stat, created = Armor.objects.get_or_create(name=armor['name'])
            armor.stats.add(stat)
        return armor

    def update(self, instance, validated_data):
        """
        Update and return an existing Armor, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.armorClass = validated_data.get('armorClass', instance.armorClass)
        instance.armorType = validated_data.get('armorType', instance.armorType)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.stealth = validated_data.get('stealth', instance.stealth)
        instance.about = validated_data.get('about', instance.about)
        instance.stats = validated_data.get('stats', instance.stats)
        instance.save()
        return instance
