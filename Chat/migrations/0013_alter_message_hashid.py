# Generated by Django 3.2.8 on 2021-11-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0012_alter_message_hashid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='hashid',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
