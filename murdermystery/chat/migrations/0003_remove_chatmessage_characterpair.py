# Generated by Django 4.2.5 on 2023-09-30 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatmessage_characterpair'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='characterpair',
        ),
    ]
