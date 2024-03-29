
from django.contrib import admin

# from . import models
from character.models import Character, Stats, Skills, LifePath, Items

# Register your models here.


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['role', 'hit_points']
    # list_editable = ['role', 'hit_points']


class StatsAdmin(admin.ModelAdmin):
    fields = (
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
    # list_display = [
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
    # ]
    # list_editable = [
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
    # ]


class SkillsAdmin(admin.ModelAdmin):
    list_display = [
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
    # list_editable = [
    #     'brawling',
    #     'evasion',
    #     'marksmanship',
    #     'melee_weapon',
    #     'concentration',
    #     'perception',
    #     'tracking',
    #     'driving',
    #     'athletics',
    #     'stealth',
    #     'basic_tech',
    #     'cybertech',
    #     'first_aid',
    #     'play_instrument',
    #     'education',
    #     'local_expert',
    #     'bribery',
    #     'conversation',
    #     'human_perception',
    #     'interrogation',
    #     'persuasion',
    # ]


class LifePathAdmin(admin.ModelAdmin):
    list_display = [
        'family',
        'motivation',
        'goals',
        'friends',
        'enemies',
        'romance',
        'personality',
    ]
    # list_editable = [
    #     'family',
    #     'motivation',
    #     'goals',
    #     'friends',
    #     'enemies',
    #     'romance',
    #     'personality',
    # ]


class ItemsAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'weight',
        'price',
        'installed',
        'slot',
        'humanity_penalty',
        'skill_modifier',
        'hands',
        'is_hidden',
        'dices',
        'dice_type',
        'ammo',
        'max_ammo',
    )


admin.site.register(Stats, StatsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(LifePath, LifePathAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Character, CharacterAdmin)
