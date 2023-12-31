# Generated by Django 4.2.7 on 2023-11-09 04:58

import character.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cyberware', '0001_initial'),
        ('gear', '0001_initial'),
        ('power', '0001_initial'),
        ('weapon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('race', models.CharField(choices=[('android', 'Android'), ('aquarian', 'Aquarian'), ('aurax', 'Aurax'), ('avion', 'Avion'), ('construct', 'Construct'), ('deader', 'Deader'), ('dwarf', 'Dwarf'), ('elf', 'Elf'), ('floran', 'Floran'), ('halfelve', 'Half-Elve'), ('halffolk', 'Half-Folk'), ('human', 'Human'), ('insectoid', 'Insectoid'), ('kalian', 'Kalian'), ('rakashan', 'Rakashan'), ('robot', 'Robot'), ('saurian', 'Saurian'), ('serran', 'Serran'), ('yeti', 'Yeti')], max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=255)),
                ('discordID', models.CharField(max_length=255)),
                ('charisma', models.IntegerField(default=0)),
                ('pace', models.IntegerField(default=0)),
                ('parry', models.IntegerField(default=0)),
                ('toughness', models.IntegerField(default=0)),
                ('attributes', models.JSONField()),
                ('skills', models.JSONField()),
                ('hindrances', models.TextField(blank=True)),
                ('edges', models.TextField(blank=True)),
                ('damage', models.JSONField(default=character.models.default_damage)),
                ('ammo', models.IntegerField(default=0)),
                ('money', models.IntegerField(default=0)),
                ('cyberware', models.ManyToManyField(blank=True, to='cyberware.cyberware')),
            ],
        ),
        migrations.CreateModel(
            name='WeaponQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.character')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_weapon', to='weapon.weapon')),
            ],
        ),
        migrations.CreateModel(
            name='GearQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.character')),
                ('gear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_gear', to='gear.gear')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='gear',
            field=models.ManyToManyField(blank=True, through='character.GearQuantity', to='gear.gear'),
        ),
        migrations.AddField(
            model_name='character',
            name='powers',
            field=models.ManyToManyField(blank=True, to='power.power'),
        ),
        migrations.AddField(
            model_name='character',
            name='weapons',
            field=models.ManyToManyField(blank=True, through='character.WeaponQuantity', to='weapon.weapon'),
        ),
    ]
