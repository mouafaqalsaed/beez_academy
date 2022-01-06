# Generated by Django 3.1.3 on 2021-06-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210605_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.CharField(choices=[('is_parents', 'Is Parents'), ('is_student', 'Is Student'), ('is_teacher ', 'Is Teacher')], max_length=190, null=True),
        ),
    ]
