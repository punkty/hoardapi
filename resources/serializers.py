from __future__ import unicode_literals
from rest_framework import serializers


from .models import (
    Armor,
    MagicProperty,
    Stats,
    Weapon,
)

class ArmorSerializer(serializers.ModelSerializer):
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
        return Armor.objects.create(**validated_data)

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
        instance.save()
        return instance

class StatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stats
        fields = (
            'id', 
            'charisma',
            'constitution', 
            'defense',
            'luck',
            'perception',
            'strength',
            'willpower',
            'wisdom',
            'armors',
            'weapons',
            )