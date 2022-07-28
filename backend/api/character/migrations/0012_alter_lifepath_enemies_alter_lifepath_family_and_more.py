# Generated by Django 4.0 on 2022-07-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0011_character_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifepath',
            name='enemies',
            field=models.CharField(max_length=2048, verbose_name='enemies'),
        ),
        migrations.AlterField(
            model_name='lifepath',
            name='family',
            field=models.CharField(max_length=2048, verbose_name='family'),
        ),
        migrations.AlterField(
            model_name='lifepath',
            name='friends',
            field=models.CharField(max_length=2048, verbose_name='friends'),
        ),
        migrations.AlterField(
            model_name='lifepath',
            name='goals',
            field=models.CharField(max_length=2048, verbose_name='goals'),
        ),
        migrations.AlterField(
            model_name='lifepath',
            name='motivation',
            field=models.CharField(max_length=2048, verbose_name='motivation'),
        ),
        migrations.AlterField(
            model_name='lifepath',
            name='personality',
            field=models.CharField(max_length=2048, verbose_name='personality'),
        ),
        migrations.AlterField(
            model_name='lifepath',
            name='romance',
            field=models.CharField(max_length=2048, verbose_name='romance'),
        ),
    ]
