# Generated by Django 4.0.2 on 2022-04-29 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicsite', '0002_janr_song_delete_janrs_delete_songs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='author',
            new_name='songname',
        ),
        migrations.RemoveField(
            model_name='janr',
            name='authors',
        ),
        migrations.AddField(
            model_name='song',
            name='janr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='musicsite.janr'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songAuthor', models.CharField(max_length=999)),
                ('janr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='musicsite.janr')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='songAuthor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='musicsite.author'),
        ),
    ]