# Generated by Django 3.1.3 on 2021-03-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_auth_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Number_auth',
            field=models.CharField(blank=True, max_length=190, null=True),
        ),
    ]
