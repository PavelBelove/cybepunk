
from django.contrib import admin

# from . import models
from backend.api.character.models import CharacterModel, StatsModel, SkillsModel, LifePathModel

# Register your models here.


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'role', 'hit_points']
    list_editable = ['user', 'role', 'hit_points']


class StatsAdmin(admin.ModelAdmin):
    list_display = [
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
    ]
    list_editable = [
        # 'stats_id',
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
    ]


class SkillsAdmin(admin.ModelAdmin):
    list_display = [
        'skills_id',
        'brawling',
        'evasion',
        'marksmanship',
        'melee_weapon',
        'concentration',
        'perception',
        'tracking',
        'driving',
        'athletics',
        'stealth',
        'basic_tech',
        'cybertech',
        'first_aid',
        'play_instrument',
        'education',
        'local_expert',
        'bribery',
        'conversation',
        'human_perception',
        'interrogation',
        'persuasion',
    ]
    list_editable = [
        # 'skills_id',
        'brawling',
        'evasion',
        'marksmanship',
        'melee_weapon',
        'concentration',
        'perception',
        'tracking',
        'driving',
        'athletics',
        'stealth',
        'basic_tech',
        'cybertech',
        'first_aid',
        'play_instrument',
        'education',
        'local_expert',
        'bribery',
        'conversation',
        'human_perception',
        'interrogation',
        'persuasion',
    ]


class LifePathAdmin(admin.ModelAdmin):
    list_display = [
        'life_path_id',
        'family',
        'motivation',
        'goals',
        'friends',
        'enemies',
        'romance',
        'personality',
    ]
    list_editable = [
        # 'life_path_id',
        'family',
        'motivation',
        'goals',
        'friends',
        'enemies',
        'romance',
        'personality',
    ]


admin.site.register(StatsModel, StatsAdmin)
admin.site.register(SkillsModel, SkillsAdmin)
admin.site.register(LifePathModel, LifePathAdmin)
admin.site.register(CharacterModel, CharacterAdmin)
