# Generated by Django 3.0.5 on 2020-05-02 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('letters', '0011_auto_20200501_1807'), ('letters', '0012_auto_20200502_0832')]

    dependencies = [
        ('institutions', '0007_auto_20200221_1956'),
        ('letters', '0010_remove_letter_address'),
        ('channels', '0006_auto_20200221_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='comment',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='excerpt',
            new_name='excerpts',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='case',
            new_name='cases',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='channel',
            new_name='channels',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='institution',
            new_name='institutions',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='description',
            new_name='descriptions',
        ),
        migrations.AlterField(
            model_name='letter',
            name='channels',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='channels.Channel', verbose_name='Channels'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='comments',
            field=models.CharField(blank=True, help_text='Comments for letter.', max_length=256, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='descriptions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='letters.Description', verbose_name='Descriptions of letter.'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='excerpts',
            field=models.CharField(blank=True, help_text='Excerpts of letter.', max_length=256, verbose_name='Excerpts'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='institutions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='institutions.Institution', verbose_name='Institutions'),
        ),
    ]
