from crypt import methods
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests import Response

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from character.serializers import CharacterSerialiser, LifePathSerialiser, SkillsSerialiser, StatsSerialiser, WeaponSerialiser
from character.models import Character, LifePath, Skills, Stats, Weapon
from character.servises import preset_stats
from character.character_data.stats.stat_presets import STATS_PRESETS

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


class TestView(APIView):
    def get(self, request, format=None):
        # lst = Stats.objects.all().values()
        # return Response({'posts': list(lst)})
        response = JsonResponse({'test': 'test'})
        # return HttpResponse("<html><body>http</body></html>")
        return response

    def post(self, request):
        post_new = Stats.objects.create(
            intel=request.data['intel'],
            ref=request.data['ref'],
            dex=request.data['dex'],
            tech=request.data['tech'],
            cool=request.data['cool'],
            will=request.data['will'],
            lusk=request.data['lusk'],
            move=request.data['move'],
            body=request.data['body'],
            emp=request.data['emp'],
        )

        return JsonResponse({'post': model_to_dict(post_new)})


# create/update/delete/read
# post/get/patch/delete
class StatsViewSet(ModelViewSet):
    serializer_class = StatsSerialiser
    queryset = Stats.objects.all()

    @action(methods=['POST'], detail=False)
    def presets(self, request):
        # serializer = StatsSerialiser(data={
        #     "id": 5,
        #     "intel": 10,
        #     "ref": 10,
        #     "dex": 8,
        #     "tech": 4,
        #     "cool": 3,
        #     "will": 8,
        #     "lusk": 6,
        #     "move": 5,
        #     "body": 6,
        #     "emp": 9
        # })
        # # print(serializer.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     # , status=status.HTTP_201_CREATED)
        #     return Response(serializer.data)
        # # , status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors)

        post_new = Stats.objects.create(
            intel=request.data['intel'],
            ref=request.data['ref'],
            dex=request.data['dex'],
            tech=request.data['tech'],
            cool=request.data['cool'],
            will=request.data['will'],
            lusk=request.data['lusk'],
            move=request.data['move'],
            body=request.data['body'],
            emp=request.data['emp'],
        )

        return JsonResponse({'post': model_to_dict(post_new)})


class SkillsViewSet(ModelViewSet):
    serializer_class = SkillsSerialiser
    queryset = Skills.objects.all()


class LifePathViewSet(ModelViewSet):
    serializer_class = LifePathSerialiser
    queryset = LifePath.objects.all()


class WeaponViewSet(ModelViewSet):
    serializer_class = WeaponSerialiser
    queryset = Weapon.objects.all()


class CharacterViewSet(ModelViewSet):
    serializer_class = CharacterSerialiser
    queryset = Character.objects.all()


if __name__ == '__main__':
    preset_stats('FIXER')
