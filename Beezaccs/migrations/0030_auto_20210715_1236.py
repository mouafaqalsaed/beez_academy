# Generated by Django 3.1.3 on 2021-07-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beezaccs', '0029_auto_20210715_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kin_exercisesonline',
            name='explanation',
            field=models.CharField(blank=True, max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='pr_exercisesonline',
            name='explanation',
            field=models.CharField(blank=True, max_length=190, null=True),
        ),
    ]