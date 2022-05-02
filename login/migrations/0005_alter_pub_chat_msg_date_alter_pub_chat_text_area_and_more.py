# Generated by Django 4.0.3 on 2022-04-21 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_pub_chat_msg_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pub_chat',
            name='msg_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Message_date'),
        ),
        migrations.AlterField(
            model_name='pub_chat',
            name='text_area',
            field=models.TextField(verbose_name='Input_text'),
        ),
        migrations.AlterField(
            model_name='pub_chat',
            name='user_name',
            field=models.CharField(max_length=20, verbose_name='Username'),
        ),
    ]
