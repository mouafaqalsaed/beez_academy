# Generated by Django 3.1.3 on 2021-07-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beezaccs', '0019_auto_20210706_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionclasssubject',
            name='title',
            field=models.CharField(max_length=190, null=True),
        ),
        migrations.AddField(
            model_name='studentsectionclasssubject',
            name='title',
            field=models.CharField(max_length=190, null=True),
        ),
    ]
