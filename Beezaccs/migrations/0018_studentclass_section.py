# Generated by Django 3.1.3 on 2021-07-06 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Beezaccs', '0017_auto_20210704_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentclass',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Section09', to='Beezaccs.section'),
        ),
    ]