from django.urls import path, include
from django.conf.urls import *
from rest_framework.routers import DefaultRouter
from character.views import index, CharacterViewSet, SkillsViewSet, StatsViewSet, LifePathViewSet, WeaponViewSet, TestView

router = DefaultRouter()
router.register(r'character', CharacterViewSet)
router.register(r'stats', StatsViewSet)
router.register(r'skills', SkillsViewSet)
router.register(r'life_path', LifePathViewSet)
router.register(r'weapon', WeaponViewSet)

app_name = 'character'
urlpatterns = [
    path('', index, name="index"),
    # path('api/v1/character/character/',
    #      CharacterViewSet.as_view({'get': 'list'})),
    # path('api/v1/character/stats/', StatsViewSet.as_view({'get': 'list'})),
    # path('api/v1/character/skills/', SkillsViewSet.as_view({'get': 'list'})),
    # path('api/v1/character/life_path/',
    #      LifePathViewSet.as_view({'get': 'list'})),
    # path('api/v1/character/weapon/',
    #      WeaponViewSet.as_view({'get': 'list'})),
    path('api/v1/character/test/',
         TestView.as_view()),

    path('api/v1/character/', include(router.urls)),
    path('api/v1/character/', include(router.urls)),
    path('api/v1/character/', include(router.urls)),
    path('api/v1/character/', include(router.urls)),
    path('api/v1/character/', include(router.urls)),


]
