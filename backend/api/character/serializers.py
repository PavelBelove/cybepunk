from rest_framework import serializers

from rest_framework.serializers import ModelSerializer, ImageField
from backend.api.character.models import CharacterModel, StatsModel, SkillsModel, LifePathModel


class StatsSerialiser(ModelSerializer):
    class Meta:
        model = StatsModel
        fields = (
            'stats_id',
            'intel',
            'ref',
            'dex',
            'tech',
            'cool',
            'will',
            'lusk',
            'move',
            'body',
            'emp',
        )


class SkillsSerialiser(ModelSerializer):
    class Meta:
        model = SkillsModel
        fields = '__all__'


class LifePathSerialiser(ModelSerializer):
    class Meta:
        model = LifePathModel
        fields = '__all__'


class CharacterSerialiser(ModelSerializer):
    class Meta:
        model = CharacterModel
        fields = '__all__'
