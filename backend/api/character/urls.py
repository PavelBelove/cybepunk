from django.urls import path, include
from django.conf.urls import *

from backend.api.character.views import CharacterView, SkillsView, StatsView, LifePathView


app_name = 'character'
urlpatterns = [
    # path('character/', CharacterView.as_view()),
    # path('stats/', StatsView.as_view()),
    # path('skills/', SkillsView.as_view()),
    # path('life_path/', LifePathView.as_view()),

    url(r'^character/$', CharacterView, name='character'),
    url(r'^stats/$', StatsView, name='stats'),
    url(r'^skills/$', SkillsView, name='skills'),
    url(r'^life_path/$', LifePathView, name='life_path'),

]
