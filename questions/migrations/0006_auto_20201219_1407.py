# Generated by Django 3.1.2 on 2020-12-19 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20201219_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='time_to_solve',
            field=models.CharField(choices=[('5 min', '5 min'), ('15 min', '15 min'), ('30 min', '30 min'), ('45 min', '45 min'), ('60 min', '60 min')], max_length=60, null=True),
        ),
    ]