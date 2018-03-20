# Generated by Django 2.0.3 on 2018-03-20 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='questions', to='categories.Category'),
        ),
    ]
