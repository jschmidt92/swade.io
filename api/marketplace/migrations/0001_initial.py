# Generated by Django 4.2.7 on 2023-11-09 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=25)),
                ('item_type', models.CharField(blank=True, max_length=25)),
                ('item_id', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True)),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.character')),
            ],
        ),
    ]
