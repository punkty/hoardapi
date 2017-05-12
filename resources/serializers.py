from rest_framework import serializers


from .models import (
    Armor,
    # MagicProperty,
    ArmorStats,
    # Weapon,
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
        armor.armorClass = validated_data.get('armorClass', armor.armorClass)
        armor.armorType = validated_data.get('armorType', armor.armorType)
        armor.weight = validated_data.get('weight', armor.weight)
        armor.stealth = validated_data.get('stealth', armor.stealth)
        armor.about = validated_data.get('about', armor.about)
        armor.stats = validated_data.get('stats', armor.stats)
        armor.save()
        return armor