from rest_framework import serializers


from .models import (
    Armor,
    ArmorStats,
    Potion,
    Trinket,
)

class ArmorStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArmorStats
        fields = (
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
    stats = ArmorStatsSerializer(many=True)

    class Meta:
        model = Armor
        fields = (
                'name',
                'price',
                'armor_class',
                'armor_type',
                'weight',
                'stealth',
                'description',
                'magical',
                'stats',
        )

    def create(self, validated_data):
        """
        Create and return a new Armor, given the validated data.
        """
        stats_data = validated_data.pop('stats')
        armor = Armor.objects.create(**validated_data)

        for stat in stats_data:
            ArmorStats.objects.create(armor=armor, **stat)
        return armor


    def update(self, armor, validated_data):
        """
        Update and return an existing Armor, given the validated data.
        """
        armor.name = validated_data.get('name', armor.name)
        armor.price = validated_data.get('price', armor.price)
        armor.armor_class = validated_data.get('armor_class', armor.armorClass)
        armor.armor_type = validated_data.get('armor_type', armor.armorType)
        armor.weight = validated_data.get('weight', armor.weight)
        armor.stealth = validated_data.get('stealth', armor.stealth)
        armor.description = validated_data.get('description', armor.description)
        armor.stats = validated_data.get('stats', armor.stats)
        armor.save()
        return armor

class PotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Potion
        fields = (
            'name',
            'effect',
            'side_effect',
            )


class TrinketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trinket
        fields = (
            'name',
            'description',
            'magical',
            'effects',
            )


