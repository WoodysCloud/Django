# Generated by Django 3.2.11 on 2022-01-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=50)),
            ],
        ),
    ]