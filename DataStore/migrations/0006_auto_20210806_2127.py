# Generated by Django 3.2.6 on 2021-08-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataStore', '0005_auto_20210804_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onefittabel',
            name='number_of_days',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='onefittabel',
            name='total_calories_burned',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
