from __future__ import unicode_literals
from rest_framework import serializers


from .models import (
    Armor,
    MagicProperty,
    ArmorStats,
    Weapon,
)

class ArmorStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArmorStats
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
    stats = ArmorStatsSerializer(many=True)

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


    # class ChangeSerializer(serializers.ModelSerializer):
    #     """Receives complex data from jira and converts into objects."""

    #     issue = JiraIssueSerializer()
    #     timestamp = TimestampField(source='created_at')

    #     class Meta:
    #         model = Change
    #         fields = ('issue', 'timestamp')

    #     def create(self, validated_data):
    #         super(serializers.ModelSerializer, self).create(validated_data=validated_data)
    #         jira_issue = JiraIssueSerializer(data=validated_data)
    #         issue = Issue.objects.get(jira_issue)
    #         self.created_at = datetime.utcnow()
    #         change = Change(**validated_data)
    #         return change



    # class JiraIssueSerializer(serializers.ModelSerializer):
    #     """Issue serializer."""
    #     id = serializers.IntegerField(source='jira_id')
    #     key = serializers.CharField(source='jira_key')
    #     summary = serializers.CharField()   ### I want field to work!
    #     # fields = serializers.DictField(child=serializers.CharField())

    #     class Meta:
    #         model = Issue
    #         fields = ('id', 'key',
    #            'summary',
    #         )

    #     def to_internal_value(self, data):
    #        # ret = super(serializers.ModelSerializer,   self).to_internal_value(data)
    #        ret = {}
    #        # ret = super().to_internal_value(data)
    #        ret['jira_id'] = data.get('id', None)
    #        ret['jira_key'] = data.get('key', None)
    #        jira_issue_fields_data = data.get('fields')
    #        if jira_issue_fields_data or 1:
    #            summary = jira_issue_fields_data.get('summary', None)
    #            ret.update(summary=summary)
    #         print('to_internal_value', ret)
    #         return ret

    #      def to_representation(self, armor):
    #         ret = {}
    #         ret = super().to_representation(armor)
    #         fields = {}
    #         fields['summary'] = armor.summary
    #         ret.update(fields=fields)
    #         print(ret)
    #         return ret