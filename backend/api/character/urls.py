from django.urls import path
from django.conf.urls import *
from character.views import index, CharacterView, SkillsView, StatsView, LifePathView

app_name = 'character'
urlpatterns = [
    path('', index, name="index"),
    path('api/v1/character/character/', CharacterView.as_view()),
    path('api/v1/character/stats/', StatsView.as_view()),
    path('api/v1/character/skills/', SkillsView.as_view()),
    path('api/v1/character/life_path/', LifePathView.as_view()),

    # url(r'^character/$', CharacterView, name='character'),
    # url(r'^stats/$', StatsView, name='stats'),
    # url(r'^skills/$', SkillsView, name='skills'),
    # url(r'^life_path/$', LifePathView, name='life_path'),
]
