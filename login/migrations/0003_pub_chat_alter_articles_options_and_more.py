# Generated by Django 4.0.3 on 2022-04-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_articles_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pub_chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='username')),
                ('text_area', models.TextField(verbose_name='input_txt')),
                ('msg_date', models.DateTimeField(verbose_name='date')),
            ],
            options={
                'verbose_name': 'Pub_chat',
                'verbose_name_plural': 'Pub_chats',
            },
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='Username'),
        ),
    ]
