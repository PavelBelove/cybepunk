from classes.character.life_path_enums import Family, Motivation, Goals, Friends, Enemies, Romance, Personality

FAMILY = {
    Family.d1: 'Ваша семья потеряла всё из-за предательства.',
    Family.d2: 'Ваша семья потеряла всё из-за плохой организации.',
    Family.d3: 'Вашу семью изгнали или иным способом лишили родного дома/страны/корпорации.',
    Family.d4: 'Вся ваша семья в тюрьме, только вы остались на свободе.',
    Family.d5: 'Ваша семья исчезла. Вы остались один.',
    Family.d6: 'Всю вашу семью убили, вы единственный выжили.',
    Family.d7: 'Ваша семья давно участвует в заговоре или вступила в тайную организацию, такую как преступный клан или группа революционеров.',
    Family.d8: 'Вашу семью разбросало по миру из-за ударов судьбы.',
    Family.d9: 'Ваша семья уже несколько поколений страдает от давней вражды.',
    Family.d10: 'Вам достались в наследство семейные долги. Придётся выплатить их, прежде чем вы начнёте жить собственной жизнью.',
}

MOTIVATION = {
    Motivation.d1: 'Деньги',
    Motivation.d2: 'Честь',
    Motivation.d3: 'Данное вами слово',
    Motivation.d4: 'Честность',
    Motivation.d5: 'Знания',
    Motivation.d6: 'Месть',
    Motivation.d7: 'Любовь',
    Motivation.d8: 'Власть',
    Motivation.d9: 'Удовольствие',
    Motivation.d10: 'Дружба'
}

GOALS = {
    Goals.d1: 'Избавиться от дурной репутации.',
    Goals.d2: 'Добиться власти и влияния.',
    Goals.d3: 'Выбраться с Улицы, чего бы это ни стоило.',
    Goals.d4: 'Причинить боль и страдания всем, кто перешёл вам дорогу.',
    Goals.d5: 'Избавиться от прошлого и постараться забыть о нём.',
    Goals.d6: 'Выследить тех, кто испортил вам жизнь, и призвать их к ответу.',
    Goals.d7: ' Получить то, что принадлежит вам по праву.',
    Goals.d8: 'По возможности спасти пострадавших членов семьи.',
    Goals.d9: 'Добиться славы и признания.',
    Goals.d10: 'Сделать так, чтобы вас боялись и уважали.'
}


FRIENDS = {
    Friends.d1: 'Как старший брат или сестра',
    Friends.d2: 'Как младший брат или сестра',
    Friends.d3: 'Учитель или наставник',
    Friends.d4: 'Партнёр или коллега',
    Friends.d5: 'Прежняя любовь',
    Friends.d6: 'Бывший враг',
    Friends.d7: 'Как отец или мать',
    Friends.d8: 'Друг детства',
    Friends.d9: 'Родственник',
    Friends.d10: 'Человек, разделяющий ваши интересы'
}

ENEMIES = {
    Enemies.d1: 'Бывший друг',
    Enemies.d2: 'Бывший любовник/любовница',
    Enemies.d3: 'Родственник',
    Enemies.d4: 'Враг с детства',
    Enemies.d5: 'Человек, работающий на вас',
    Enemies.d6: 'Человек, на которого вы работаете',
    Enemies.d7: 'Партнёр или коллега',
    Enemies.d8: 'Кто-то из банды бустеров',
    Enemies.d9: 'Менеджер из корпорации',
    Enemies.d10: 'Чиновник из правительства'
}

ROMANCE = {
    Romance.d1: 'Ваш любимый(ая) погиб от несчастного случая.',
    Romance.d2: 'Ваш любимый(ая) исчез при загадочных обстоятельствах.',
    Romance.d3: 'Просто не срослось.',
    Romance.d4: 'Между вами встали личные интересы или вендетта.',
    Romance.d5: 'Вашего любимого(ую) похитили.',
    Romance.d6: 'Ваш любимый(ая) сошёл с ума.',
    Romance.d7: 'Ваш любимый(ая) покончил с собой.',
    Romance.d8: 'Ваш любимый(ая) погиб в бою.',
    Romance.d9: 'Соперник увёл у вас партнёра.',
    Romance.d10: 'Ваш любимый(ая) в тюрьме или в изгнании.'
}

PERSONALITY = {
    Personality.d1: 'Застенчивый и скрытный',
    Personality.d2: 'Неуживчивый, жестокий, непокорный',
    Personality.d3: 'Высокомерный, гордый и замкнутый',
    Personality.d4: 'Непостоянный, безрассудный и упрямый',
    Personality.d5: 'Придирчивый, капризный и раздражительный',
    Personality.d6: 'Серьёзный и постоянный',
    Personality.d7: 'Глуповатый и легкомысленный',
    Personality.d8: 'Подлый и лживый',
    Personality.d9: 'Умный и отстранённый',
    Personality.d10: 'Дружелюбный и общительный'
}

life_path_exemples = [
    {'Family': 'd5', 'Motivation': 'd7', 'Goals': 'd7', 'Friends': [],
        'Enemies': ['d2'], 'Romance': 'd6', 'Personality': 'd5'},
    {'Family': 'd1', 'Motivation': 'd5', 'Goals': 'd9', 'Friends': [],
        'Enemies': [], 'Romance': 'd3', 'Personality': 'd3'},
    {'Family': 'd', 'Motivation': 'd8', 'Goals': 'd9', 'Friends': [],
        'Enemies': ['d', 'd6'], 'Romance': 'd7', 'Personality': 'd8'},
    {'Family': 'd', 'Motivation': 'd8', 'Goals': 'd7', 'Friends': [],
        'Enemies': [], 'Romance': 'd4', 'Personality': 'd8'},
    {'Family': 'd', 'Motivation': 'd8', 'Goals': 'd6', 'Friends': [],
        'Enemies': ['d'], 'Romance': 'd5', 'Personality': 'd4'},
    {'Family': 'd9', 'Motivation': 'd2', 'Goals': 'd5', 'Friends': [],
        'Enemies': [], 'Romance': 'd1', 'Personality': 'd6'},
    {'Family': 'd4', 'Motivation': 'd1', 'Goals': 'd3', 'Friends': [],
        'Enemies': ['d3', 'd4', 'd', 'd9'], 'Romance': 'd6', 'Personality': 'd9'},
    {'Family': 'd1', 'Motivation': 'd5', 'Goals': 'd2', 'Friends': [
        'd9'], 'Enemies': [], 'Romance': 'd1', 'Personality': 'd3'},
    {'Family': 'd8', 'Motivation': 'd3', 'Goals': 'd3', 'Friends': [
        'd1', 'd7'], 'Enemies': [], 'Romance': 'd8', 'Personality': 'd8'},
    {'Family': 'd5', 'Motivation': 'd7', 'Goals': 'd', 'Friends': [],
        'Enemies': [], 'Romance': 'd6', 'Personality': 'd4'},
    {'Family': 'd2', 'Motivation': 'd6', 'Goals': 'd5', 'Friends': [],
        'Enemies': [], 'Romance': 'd4', 'Personality': 'd5'},
    {'Family': 'd1', 'Motivation': 'd5', 'Goals': 'd6', 'Friends': [
        'd', 'd7', 'd'], 'Enemies': ['d', 'd7'], 'Romance': 'd2', 'Personality': 'd8'},
    {'Family': 'd9', 'Motivation': 'd', 'Goals': 'd8', 'Friends': [],
        'Enemies': [], 'Romance': 'd1', 'Personality': 'd1'},
    {'Family': 'd1', 'Motivation': 'd3', 'Goals': 'd3', 'Friends': [],
        'Enemies': ['d8', 'd8', 'd5', 'd8'], 'Romance': 'd5', 'Personality': 'd'},
    {'Family': 'd8', 'Motivation': 'd4', 'Goals': 'd8', 'Friends': [],
        'Enemies': [], 'Romance': 'd7', 'Personality': 'd9'},
    {'Family': 'd2', 'Motivation': 'd9', 'Goals': 'd5', 'Friends': [],
        'Enemies': [], 'Romance': 'd1', 'Personality': 'd9'},
    {'Family': 'd9', 'Motivation': 'd4', 'Goals': 'd9', 'Friends': [],
        'Enemies': [], 'Romance': 'd4', 'Personality': 'd2'},
    {'Family': 'd1', 'Motivation': 'd7', 'Goals': 'd3', 'Friends': [],
        'Enemies': [], 'Romance': 'd1', 'Personality': 'd7'},
    {'Family': 'd2', 'Motivation': 'd8', 'Goals': 'd6', 'Friends': [
        'd8', 'd7', 'd6'], 'Enemies': ['d3', 'd5'], 'Romance': 'd7', 'Personality': 'd1'},
    {'Family': 'd2', 'Motivation': 'd7', 'Goals': 'd1', 'Friends': [],
        'Enemies': [], 'Romance': 'd', 'Personality': 'd8'}
]
