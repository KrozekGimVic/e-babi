# Generated by Django 3.1.3 on 2020-11-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='label',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]