from rest_framework import serializers


from .models import (
    Armor,
    ArmorStats,
    Mount,
    Potion,
    Tool,
    Trinket,
    Weapon,
    WeaponStats,

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
                'type',
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
        armor.armor_class = validated_data.get('armor_class', armor.armor_class)
        armor.type = validated_data.get('type', armor.type)
        armor.weight = validated_data.get('weight', armor.weight)
        armor.stealth = validated_data.get('stealth', armor.stealth)
        armor.description = validated_data.get('description', armor.description)
        armor.stats = validated_data.get('stats', armor.stats)
        armor.save()
        return armor


class MountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mount
        fields = (
            'name',
            'nickname',
            'type',
            'speed',
            'max_burden',
            'price',
            'health',
            'description'
            )


class PotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Potion
        fields = (
            'name',
            'effect',
            'side_effect',
            )

class ToolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tool
        fields = (
            'name',
            'description',
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


class WeaponStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeaponStats
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


class WeaponSerializer(serializers.ModelSerializer):
    stats = WeaponStatsSerializer(many=True)
    class Meta:
        model = Weapon
        fields = (
            'name',
            'price',
            'damage',
            'type',
            'weight',
            'stealth',
            'description',
            'magical'
            )
    def create(self, validated_data):
        """
        Create and return a new Armor, given the validated data.
        """
        stats_data = validated_data.pop('stats')
        weapon = Weapon.objects.create(**validated_data)

        for stat in stats_data:
            WeaponStats.objects.create(weapon=weapon, **stat)
        return weapon


    def update(self, weapon, validated_data):
        """
        Update and return an existing Armor, given the validated data.
        """
        weapon.name = validated_data.get('name', weapon.name)
        weapon.price = validated_data.get('price', weapon.price)
        weapon.damage = validated_data.get('damage', weapon.damage)
        weapon.type = validated_data.get('type', weapon.type)
        weapon.weight = validated_data.get('weight', weapon.weight)
        weapon.stealth = validated_data.get('stealth', weapon.stealth)
        weapon.description = validated_data.get('description', weapon.description)
        weapon.stats = validated_data.get('stats', weapon.stats)
        weapon.save()
        return weapon
