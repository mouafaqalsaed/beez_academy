# Generated by Django 3.1.3 on 2021-07-15 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beezaccs', '0028_auto_20210715_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='mid_exercisesonline',
            name='alternative_image',
            field=models.CharField(blank=True, max_length=190, null=True),
        ),
        migrations.AddField(
            model_name='mid_exercisesonline',
            name='explanation',
            field=models.CharField(max_length=190, null=True),
        ),
    ]
