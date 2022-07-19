from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Stats(models.Model):
    u'''Model Class'''

    class Meta:
        u'''Model Meta'''
        verbose_name = "Статы"
        verbose_name_plural = "Статы"

    intel = models.IntegerField(verbose_name='intel', default=5)
    ref = models.IntegerField(verbose_name='ref', default=5)
    dex = models.IntegerField(verbose_name='dex', default=5)
    tech = models.IntegerField(verbose_name='tech', default=5)
    cool = models.IntegerField(verbose_name='cool', default=5)
    will = models.IntegerField(verbose_name='will', default=5)
    lusk = models.IntegerField(verbose_name='lusk', default=5)
    move = models.IntegerField(verbose_name='move', default=5)
    body = models.IntegerField(verbose_name='body', default=5)
    emp = models.IntegerField(verbose_name='emp', default=5)

    def as_json(self):
        u'''Returns Model as JSON'''
        return dict(
            intel=self.intel,
            ref=self.ref,
            dex=self.dex,
            tech=self.tech,
            cool=self.cool,
            will=self.will,
            lusk=self.lusk,
            move=self.move,
            body=self.body,
            emp=self.emp,
        )

    # def __str__(self):
    #     return self.name


class Skills(models.Model):
    u'''Model Class'''
    class Meta:
        u'''Model Meta'''
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    brawling = models.IntegerField(verbose_name='brawling', default=5)
    evasion = models.IntegerField(verbose_name='evasion', default=5)
    marksmanship = models.IntegerField(verbose_name='marksmanship', default=5)
    melee_weapon = models.IntegerField(verbose_name='melee_weapon', default=5)
    concentration = models.IntegerField(
        verbose_name='concentration', default=5)
    perception = models.IntegerField(verbose_name='perception', default=5)
    tracking = models.IntegerField(verbose_name='tracking', default=5)
    driving = models.IntegerField(verbose_name='driving', default=5)
    athletics = models.IntegerField(verbose_name='athletics', default=5)
    stealth = models.IntegerField(verbose_name='stealth', default=5)
    basic_tech = models.IntegerField(verbose_name='basic_tech', default=5)
    cybertech = models.IntegerField(verbose_name='cybertech', default=5)
    first_aid = models.IntegerField(verbose_name='first_aid', default=5)
    play_instrument = models.IntegerField(
        verbose_name='play_instrument', default=5)
    education = models.IntegerField(verbose_name='education', default=5)
    local_expert = models.IntegerField(verbose_name='local_expert', default=5)
    bribery = models.IntegerField(verbose_name='bribery', default=5)
    conversation = models.IntegerField(verbose_name='conversation', default=5)
    human_perception = models.IntegerField(
        verbose_name='human_perception', default=5)
    interrogation = models.IntegerField(
        verbose_name='interrogation', default=5)
    persuasion = models.IntegerField(verbose_name='persuasion', default=5)

    def as_json(self):
        u'''Returns Model as JSON'''
        return dict(
            skills_id=self.skills_id,
            brawling=self.brawling,
            evasion=self.evasion,
            marksmanship=self.marksmanship,
            melee_weapon=self.melee_weapon,
            concentration=self.concentration,
            perception=self.perception,
            tracking=self.tracking,
            driving=self.driving,
            athletics=self.athletics,
            stealth=self.stealth,
            basic_tech=self.basic_tech,
            cybertech=self.cybertech,
            first_aid=self.first_aid,
            play_instrument=self.play_instrument,
            education=self.education,
            local_expert=self.local_expert,
            bribery=self.bribery,
            conversation=self.conversation,
            human_perception=self.human_perception,
            interrogation=self.interrogation,
            persuasion=self.persuasion,
        )

    # def __str__(self):
    #     return self.name


class LifePath(models.Model):
    u'''Model Class'''

    class Meta:
        u'''Model Meta'''

        verbose_name = "Жизненный путь"
        verbose_name_plural = "Жизненные пути"

    FAMILY = (
        (1, 'Ваша семья потеряла всё из-за предательства.'),
        (2, 'Ваша семья потеряла всё из-за плохой организации.'),
        (3, 'Вашу семью изгнали или иным способом лишили родного дома/страны/корпорации.'),
        (4, 'Вся ваша семья в тюрьме, только вы остались на свободе.'),
        (5, 'Ваша семья исчезла. Вы остались один.'),
        (6, 'Всю вашу семью убили, вы единственный выжили.'),
        (7, 'Ваша семья давно участвует в заговоре или вступила в тайную организацию, такую как преступный клан или группа революционеров.'),
        (8, 'Вашу семью разбросало по миру из-за ударов судьбы.'),
        (9, 'Ваша семья уже несколько поколений страдает от давней вражды.'),
        (10, 'Вам достались в наследство семейные долги. Придётся выплатить их, прежде чем вы начнёте жить собственной жизнью.'),
    )

    MOTIVATION = (
        (1, 'Деньги'),
        (2, 'Честь'),
        (3, 'Данное вами слово'),
        (4, 'Честность'),
        (5, 'Знания'),
        (6, 'Месть'),
        (7, 'Любовь'),
        (8, 'Власть'),
        (9, 'Удовольствие'),
        (10, 'Дружба'),
    )

    GOALS = (
        (1, 'Избавиться от дурной репутации.'),
        (2, 'Добиться власти и влияния.'),
        (3, 'Выбраться с Улицы, чего бы это ни стоило.'),
        (4, 'Причинить боль и страдания всем, кто перешёл вам дорогу.'),
        (5, 'Избавиться от прошлого и постараться забыть о нём.'),
        (6, 'Выследить тех, кто испортил вам жизнь, и призвать их к ответу.'),
        (7, ' Получить то, что принадлежит вам по праву.'),
        (8, 'По возможности спасти пострадавших членов семьи.'),
        (9, 'Добиться славы и признания.'),
        (10, 'Сделать так, чтобы вас боялись и уважали.'),
    )

    FRIENDS = (
        (1, 'Как старший брат или сестра'),
        (2, 'Как младший брат или сестра'),
        (3, 'Учитель или наставник'),
        (4, 'Партнёр или коллега'),
        (5, 'Прежняя любовь'),
        (6, 'Бывший враг'),
        (7, 'Как отец или мать'),
        (8, 'Друг детства'),
        (9, 'Родственник'),
        (10, 'Человек, разделяющий ваши интересы'),
    )

    ENEMIES = (
        (1, 'Бывший друг'),
        (2, 'Бывший любовник/любовница'),
        (3, 'Родственник'),
        (4, 'Враг с детства'),
        (5, 'Человек, работающий на вас'),
        (6, 'Человек, на которого вы работаете'),
        (7, 'Партнёр или коллега'),
        (8, 'Кто-то из банды бустеров'),
        (9, 'Менеджер из корпорации'),
        (10, 'Чиновник из правительства'),
    )

    ROMANCE = (
        (1, 'Ваш любимый(ая) погиб от несчастного случая.'),
        (2, 'Ваш любимый(ая) исчез при загадочных обстоятельствах.'),
        (3, 'Просто не срослось.'),
        (4, 'Между вами встали личные интересы или вендетта.'),
        (5, 'Вашего любимого(ую) похитили.'),
        (6, 'Ваш любимый(ая) сошёл с ума.'),
        (7, 'Ваш любимый(ая) покончил с собой.'),
        (8, 'Ваш любимый(ая) погиб в бою.'),
        (9, 'Соперник увёл у вас партнёра.'),
        (10, 'Ваш любимый(ая) в тюрьме или в изгнании.'),
    )

    PERSONALITY = (
        (1, 'Застенчивый и скрытный'),
        (2, 'Неуживчивый, жестокий, непокорный'),
        (3, 'Высокомерный, гордый и замкнутый'),
        (4, 'Непостоянный, безрассудный и упрямый'),
        (5, 'Придирчивый, капризный и раздражительный'),
        (6, 'Серьёзный и постоянный'),
        (7, 'Глуповатый и легкомысленный'),
        (8, 'Подлый и лживый'),
        (9, 'Умный и отстранённый'),
        (10, 'Дружелюбный и общительный'),
    )

    family = models.IntegerField(verbose_name='family',
                                 choices=FAMILY)
    motivation = models.IntegerField(
        verbose_name='motivation', choices=MOTIVATION)
    goals = models.IntegerField(verbose_name='goals',
                                choices=GOALS)
    friends = models.IntegerField(
        verbose_name='friends', choices=FRIENDS)
    enemies = models.IntegerField(
        verbose_name='enemies', choices=ENEMIES)
    romance = models.IntegerField(
        verbose_name='romance', choices=ROMANCE)
    personality = models.IntegerField(
        verbose_name='personality', choices=PERSONALITY)

    def as_json(self):
        u'''Returns Model as JSON'''
        return dict(
            life_path_id=self.life_path_id,
            family=self.family,
            motivation=self.motivation,
            goals=self.goals,
            friends=self.friends,
            enemies=self.enemies,
            romance=self.romance,
            personality=self.personality,
        )

    # def __str__(self):
    #     return self.name


# class Ammo(models.Model):
#     u'''Model Class'''

#     class Meta:
#         u'''Model Meta'''
#         verbose_name = "Боеприпас"
#         verbose_name_plural = "Боеприпасы"

#     name = models.CharField(verbose_name='hit_points', max_length=64)
#     price = models.IntegerField(verbose_name='intel', default=5)
#     quantyty = models.IntegerField(verbose_name='intel', default=12)

#     def as_json(self):
#         u'''Returns Model as JSON'''
#         return dict(
#             name=self.name,
#             price=self.price,
#             quantyty=self.quantyty,
#         )

#     def __str__(self):
#         return self.name


class Weapon(models.Model):
    u'''Model Class'''

    class Meta:
        u'''Model Meta'''
        verbose_name = "Оружие"
        verbose_name_plural = "Оружие"

    MASS = (
        (0, 'implant'),
        (1, 'light'),
        (2, 'medium'),
        (3, 'heavy'),
    )

    HANDS = (
        (0, 'implant'),
        (1, 'one'),
        (2, 'Two'),
    )

    DISES = zip(range(1, 5), range(1, 5))

    DISES_TYPE = (
        (0, 'd6'),
        (1, 'd10'),
    )

    AMMO = zip(range(1, 30), range(1, 30))

    name = models.CharField(verbose_name='hit_points', max_length=64)
    mass = models.IntegerField(verbose_name='mass', choices=MASS)
    hands = models.IntegerField(verbose_name='hands', choices=HANDS)
    price = models.IntegerField(verbose_name='intel', default=50)
    is_hidden = models.BooleanField(default=False)
    dices = models.IntegerField(verbose_name='dises', choices=DISES)
    dice_type = models.IntegerField(
        verbose_name='dises_type', choices=DISES_TYPE)
    ammo = models.IntegerField(verbose_name='ammo', choices=AMMO)
    max_ammo = models.IntegerField(verbose_name='max_ammo', choices=AMMO)

    def as_json(self):
        u'''Returns Model as JSON'''
        return dict(
            name=self.name,
            mass=self.mass,
            hands=self.hands,
            price=self.price,
            is_hidden=self.is_hidden,
            dices=self.dices,
            dice_type=self.dice_type,
            ammo=self.ammo,
            max_ammo=self.max_ammo,
        )

    def __str__(self):
        return self.name


class Character(models.Model):
    class Meta:
        u'''Model Meta'''
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    ROLES = (
        (1, 'FIXER'),
        (2, 'ROCKERBOY'),
        (3, 'SOLO'),
        (4, 'NETRUNNER'),
        (5, 'NOMAD'),
        (6, 'TECH'),
        (7, 'COP'),
        (8, 'CORPORATE'),
        (9, 'MEDIC'),
        (10, 'JOUNALIST'),
    )
    user = models.ForeignKey(User, verbose_name='user',
                             on_delete=models.CASCADE)
    name = models.CharField(verbose_name='hit_points',
                            max_length=64, default='Punk')
    role = models.IntegerField(verbose_name='role', choices=ROLES)
    skills = models.ForeignKey(
        'Skills', verbose_name='skills', on_delete=models.CASCADE)
    life_path = models.ForeignKey('LifePath',
                                  verbose_name='life_path', on_delete=models.CASCADE)
    stats = models.ForeignKey(
        'Stats', verbose_name='stats', on_delete=models.CASCADE)
    hit_points = models.CharField(verbose_name='hit_points', max_length=64)

    max_hit_points = models.CharField(
        verbose_name='max_hit_points', max_length=64)

    left_hand_weapon = models.CharField(
        verbose_name='left_hand_weapon', max_length=64)
    right_hand_weapon = models.CharField(
        verbose_name='right_hand_weapon', max_length=64)
    inventory = models.CharField(verbose_name='inventory', max_length=64)

    def as_json(self):
        u'''Returns Model as JSON'''
        return dict(
            user=self.user,
            name=self.name,
            role=self.role,
            skills=self.skills,
            life_path=self.life_path,
            stats=self.stats,
            hit_points=self.hit_points,
            max_hit_points=self.max_hit_points,
            left_hand_weapon=self.left_hand_weapon,
            right_hand_weapon=self.right_hand_weapon,
            inventory=self.inventory,
        )
