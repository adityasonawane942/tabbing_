# Generated by Django 2.2.1 on 2019-06-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190620_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='team1',
            field=models.CharField(max_length=100, null=True),
        ),
    ]