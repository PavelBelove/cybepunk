# Generated by Django 4.0 on 2022-07-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0009_alter_character_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='hit_points')),
                ('mass', models.IntegerField(choices=[(0, 'implant'), (1, 'light'), (2, 'medium'), (3, 'heavy')], verbose_name='mass')),
                ('hands', models.IntegerField(choices=[(0, 'implant'), (1, 'one'), (2, 'Two')], verbose_name='hands')),
                ('price', models.IntegerField(default=50, verbose_name='intel')),
                ('is_hidden', models.BooleanField(default=False)),
                ('dices', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], verbose_name='dises')),
                ('dice_type', models.IntegerField(choices=[(0, 'd6'), (1, 'd10')], verbose_name='dises_type')),
                ('ammo', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29)], verbose_name='ammo')),
                ('max_ammo', models.IntegerField(choices=[], verbose_name='max_ammo')),
            ],
            options={
                'verbose_name': 'Оружие',
                'verbose_name_plural': 'Оружие',
            },
        ),
    ]
