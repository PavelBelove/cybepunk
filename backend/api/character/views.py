from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from backend.api.character.serializers import CharacterSerialiser, LifePathSerialiser, SkillsSerialiser, StatsSerialiser


# Create your views here.


class StatsView(generics.CreateAPIView):
    serializer_class = StatsSerialiser()


class SkillsView(generics.CreateAPIView):
    serializer_class = SkillsSerialiser()


class LifePathView(generics.CreateAPIView):
    serializer_class = LifePathSerialiser()


class CharacterView(generics.CreateAPIView):
    serializer_class = CharacterSerialiser()
