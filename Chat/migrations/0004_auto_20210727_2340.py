# Generated by Django 3.2.5 on 2021-07-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0003_users_hashid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=150)),
                ('reciever', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Contects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('you', models.CharField(max_length=150)),
                ('contect', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='hashid',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='users',
            name='passwd',
            field=models.CharField(max_length=150),
        ),
    ]
