# Generated by Django 3.1.5 on 2021-04-17 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0004_auto_20210417_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitelink',
            name='target_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='link.target'),
        ),
        migrations.AlterField(
            model_name='target',
            name='parent_id',
            field=models.IntegerField(default=-1, null=True),
        ),
    ]
