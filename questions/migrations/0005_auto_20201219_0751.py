# Generated by Django 3.1.2 on 2020-12-19 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_remove_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='menthor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.solveform'),
        ),
    ]