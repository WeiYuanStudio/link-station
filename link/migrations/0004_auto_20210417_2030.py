# Generated by Django 3.1.5 on 2021-04-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_auto_20210124_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='description',
            field=models.TextField(max_length=1020, null=True),
        ),
        migrations.AddField(
            model_name='websitetype',
            name='can_format',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='websitetype',
            name='format_template',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='websitetype',
            name='source_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]
