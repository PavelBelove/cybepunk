# Generated by Django 4.0 on 2022-07-16 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0004_lifepath_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(1, 'FIXER'), (2, 'ROCKERBOY'), (3, 'SOLO'), (4, 'NETRUNNER'), (5, 'NOMAD'), (6, 'TECH'), (7, 'COP'), (8, 'CORPORATE'), (9, 'MEDIC'), (10, 'JOUNALIST')], verbose_name='role')),
                ('hit_points', models.CharField(max_length=64, verbose_name='hit_points')),
                ('max_hit_points', models.CharField(max_length=64, verbose_name='max_hit_points')),
                ('left_hand_weapon', models.CharField(max_length=64, verbose_name='left_hand_weapon')),
                ('right_hand_weapon', models.CharField(max_length=64, verbose_name='right_hand_weapon')),
                ('inventory', models.CharField(max_length=64, verbose_name='inventory')),
                ('life_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.lifepath', verbose_name='life_path')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.skills', verbose_name='skills')),
                ('stats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.stats', verbose_name='stats')),
            ],
        ),
    ]
