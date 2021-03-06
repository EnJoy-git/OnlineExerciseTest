# Generated by Django 3.0.7 on 2020-06-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsystem', '0002_auto_20200622_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='blank_question',
            name='value',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2, verbose_name='分值'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mc_question',
            name='value',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2, verbose_name='分值'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sc_question',
            name='value',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2, verbose_name='分值'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='分数'),
        ),
    ]
