# Generated by Django 4.0 on 2022-07-28 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('character', '0012_alter_lifepath_enemies_alter_lifepath_family_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='user'),
        ),
    ]
