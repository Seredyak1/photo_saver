# Generated by Django 3.2.6 on 2021-08-29 08:42

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_saver', '0004_auto_20210824_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedimage',
            name='color',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='savedimage',
            name='downloads_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='savedimage',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='savedimage',
            name='user',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='savedimage',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
