# Generated by Django 3.1.5 on 2021-01-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='parent_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='target',
            name='type',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='websitelink',
            name='type',
            field=models.IntegerField(null=True),
        ),
    ]
