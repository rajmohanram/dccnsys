# Generated by Django 2.1.7 on 2019-03-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_profile_agree_to_receive_emails'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_version',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
    ]
