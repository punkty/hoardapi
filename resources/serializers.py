from rest_framework import serializers


from .models import (
    Armor,
    ArmorStats,
    MagicalProperty,
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
            'intelligence',
            'luck',
            'perception',
            'strength',
            'wisdom',
            )

class ArmorSerializer(serializers.ModelSerializer):
    stats = ArmorStatsSerializer(many=True)
    class Meta:
        model = Armor
        fields = (
                'id',
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

class MagicalPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = MagicalProperty
        fields = (
            'id',
            'name',
            'description',
        )

class MagicalWeaponPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = MagicalProperty
        fields = (
            'name',
        )


class MountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mount
        fields = (
            'id',
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
            'id',
            'name',
            'effect',
            'side_effect',
            )

class ToolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tool
        fields = (
            'id',
            'name',
            'description',
            )


class TrinketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trinket
        fields = (
            'id',
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
            'intelligence',
            'luck',
            'perception',
            'strength',
            'wisdom',
            )


class WeaponSerializer(serializers.ModelSerializer):
    stats = WeaponStatsSerializer(many=True)
    magical_properties = MagicalWeaponPropertySerializer(many=True)
    class Meta:
        model = Weapon
        fields = (
            'id',
            'name',
            'price',
            'damage',
            'range',
            'type',
            'weight',
            'stealth',
            'description',
            'magical',
            'magical_properties',
            'stats',
            )
    def create(self, validated_data):
        """
        Create and return a new Armor, given the validated data.
        """
        stats_data = validated_data.pop('stats')
        magical_property_data = validated_data.pop('magical_properties')
        weapon = Weapon.objects.create(**validated_data)

        for stat in stats_data:
            WeaponStats.objects.create(weapon=weapon, **stat)

        for magical_property in magical_property_data:
            MagicalProperty.objects.create(weapon=weapon, **magical_property)

        return weapon


    def update(self, weapon, validated_data):
        """
        Update and return an existing Armor, given the validated data.
        """
        weapon.name = validated_data.get('name', weapon.name)
        weapon.price = validated_data.get('price', weapon.price)
        weapon.damage = validated_data.get('damage', weapon.damage)
        weapon.range = validated_data.get('range', weapon.range)
        weapon.type = validated_data.get('type', weapon.type)
        weapon.weight = validated_data.get('weight', weapon.weight)
        weapon.stealth = validated_data.get('stealth', weapon.stealth)
        weapon.description = validated_data.get('description', weapon.description)
        weapon.stats = validated_data.get('stats', weapon.stats)
        weapon.save()
        return weapon
