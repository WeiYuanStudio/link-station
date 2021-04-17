# Generated by Django 3.1.5 on 2021-04-17 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('link', '0001_initial'), ('link', '0002_auto_20210124_1813'), ('link', '0003_auto_20210124_2234'), ('link', '0004_auto_20210417_2030'), ('link', '0005_auto_20210417_2045'), ('link', '0006_auto_20210417_2051'), ('link', '0007_auto_20210417_2055')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TargetType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '对象类型',
                'verbose_name_plural': '对象类型',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('parent_id', models.IntegerField(default=-1, null=True)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='link.targettype')),
                ('description', models.TextField(max_length=1020, null=True)),
            ],
            options={
                'verbose_name': '对象',
                'verbose_name_plural': '对象',
            },
        ),
        migrations.CreateModel(
            name='WebSiteType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('can_format', models.BooleanField(default=False)),
                ('format_template', models.CharField(default=None, max_length=255, null=True)),
                ('source_url', models.CharField(default='', max_length=255)),
            ],
            options={
                'verbose_name': '站点类型',
                'verbose_name_plural': '站点类型',
            },
        ),
        migrations.CreateModel(
            name='WebSiteLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='link.websitetype')),
                ('target_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='link.target')),
            ],
            options={
                'verbose_name': '站点链接',
                'verbose_name_plural': '站点链接',
            },
        ),
    ]