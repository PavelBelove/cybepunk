# Generated by Django 4.0 on 2022-08-13 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_alter_character_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='in_hands',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Hands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.character', verbose_name='character')),
                ('left_hand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Left', to='character.items', verbose_name='left_hand')),
                ('right_hand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Right', to='character.items', verbose_name='right_hand')),
            ],
            options={
                'verbose_name': 'Рука',
                'verbose_name_plural': 'Руки',
            },
        ),
    ]