# Generated by Django 2.2.1 on 2019-07-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_message_my_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]