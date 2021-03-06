# Generated by Django 2.1.1 on 2018-09-08 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NamePlayer', models.CharField(max_length=255)),
                ('Detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameStadium', models.CharField(max_length=255)),
                ('Detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameTeam', models.CharField(max_length=255)),
                ('NumberPlayers', models.IntegerField()),
                ('Detalle', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='stadium',
            name='Id_Team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExamenApp.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='Id_Team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExamenApp.Team'),
        ),
    ]
