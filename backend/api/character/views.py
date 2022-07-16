from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from character.serializers import CharacterSerialiser, LifePathSerialiser, SkillsSerialiser, StatsSerialiser


# Create your views here.

# def random_character(request):
#     # https://cybertext/api/v1/character/random?character_type=fixer
#     charater_type = request.get_param('character_type')
#     print(character_type)  # fixer

#     character_factory = CharacterFactory()

#     character_data = character_factory.create_character()

#     character = Character(
#         role=character_data["role"]
#         # ...
#     )

#     character.save()

#     # JsonView()

#     return character.to_json(character)

# def create_character(request):
#     # https://cybertext/api/v1/character/random?character_type=fixer
#     charater_type = request.get_param('character_type')
#     print(character_type) #fixer

#     character_factory = CharacterFactory()

#     # JsonView()

#     return character.to_json('')


def index(request):
    return HttpResponse("<html><body>Works</body></html>")


# create/update/delete/read
# post/get/patch/delete
class StatsView(generics.CreateAPIView):
    serializer_class = StatsSerialiser()


class SkillsView(generics.CreateAPIView):
    serializer_class = SkillsSerialiser()


class LifePathView(generics.CreateAPIView):
    serializer_class = LifePathSerialiser()


class CharacterView(generics.CreateAPIView):
    serializer_class = CharacterSerialiser()
