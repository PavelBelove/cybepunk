from rest_framework import serializers

from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from character.models import Character, Stats, Skills, LifePath, Weapon


class StatsSerialiser(ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'
        # (
        #     'stats_id',
        #     'intel',
        #     'ref',
        #     'dex',
        #     'tech',
        #     'cool',
        #     'will',
        #     'lusk',
        #     'move',
        #     'body',
        #     'emp',
        # )


class SkillsSerialiser(ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class LifePathSerialiser(ModelSerializer):
    class Meta:
        model = LifePath
        fields = '__all__'


class WeaponSerialiser(ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class CharacterSerialiser(ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
