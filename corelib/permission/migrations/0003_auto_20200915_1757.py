# Generated by Django 3.0.6 on 2020-09-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0002_apipermission'),
    ]

    operations = [
        migrations.AddField(
            model_name='apipermission',
            name='realname',
            field=models.CharField(default='', max_length=64, verbose_name='中文姓名'),
        ),
        migrations.AlterField(
            model_name='apipermission',
            name='perm_group',
            field=models.CharField(default='', max_length=64, verbose_name='权限属组'),
        ),
    ]
