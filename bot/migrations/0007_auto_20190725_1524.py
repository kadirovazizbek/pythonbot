# Generated by Django 2.2.1 on 2019-07-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_auto_20190725_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='next_command',
            field=models.CharField(max_length=255, null=True, verbose_name='next_command'),
        ),
        migrations.AlterField(
            model_name='message',
            name='previous_command',
            field=models.CharField(max_length=255, null=True, verbose_name='prev_command'),
        ),
    ]
