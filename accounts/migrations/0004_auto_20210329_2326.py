# Generated by Django 3.1.3 on 2021-03-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_number_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Number_auth',
            field=models.CharField(blank=True, default='1', max_length=190, null=True),
        ),
    ]
