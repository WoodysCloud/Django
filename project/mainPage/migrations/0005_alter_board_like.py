# Generated by Django 3.2.11 on 2022-01-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0004_alter_board_registered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='like',
            field=models.IntegerField(null=True),
        ),
    ]
