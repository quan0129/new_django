# Generated by Django 3.1 on 2020-09-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_facebookuser_facebook_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookuser',
            name='is_email',
            field=models.BooleanField(default=True),
        ),
    ]
