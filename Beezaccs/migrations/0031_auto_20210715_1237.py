# Generated by Django 3.1.3 on 2021-07-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beezaccs', '0030_auto_20210715_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mid_exercisesonline',
            name='explanation',
            field=models.CharField(blank=True, max_length=190, null=True),
        ),
    ]
