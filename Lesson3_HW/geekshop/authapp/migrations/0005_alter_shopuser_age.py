# Generated by Django 3.2 on 2021-06-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_shopuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=18, verbose_name='возраст'),
        ),
    ]
