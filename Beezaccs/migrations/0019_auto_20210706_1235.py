# Generated by Django 3.1.3 on 2021-07-06 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Beezaccs', '0018_studentclass_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionClassSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kgclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Classes03', to='Beezaccs.classes')),
                ('kgsubject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject07', to='Beezaccs.kin_categoriesclass')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level03', to='Beezaccs.level')),
                ('midclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Classes05', to='Beezaccs.mid_classes')),
                ('midsubject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject09', to='Beezaccs.mid_subject')),
                ('prclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Classes04', to='Beezaccs.pr_classes')),
                ('prsubject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject08', to='Beezaccs.pr_subject')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Section09', to='Beezaccs.section')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSectionClassSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('secionClass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SectionClassSubject01', to='Beezaccs.sectionclasssubject')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student05', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentclass',
            name='kgclass',
        ),
        migrations.RemoveField(
            model_name='studentclass',
            name='level',
        ),
        migrations.RemoveField(
            model_name='studentclass',
            name='midclass',
        ),
        migrations.RemoveField(
            model_name='studentclass',
            name='prclass',
        ),
        migrations.RemoveField(
            model_name='studentclass',
            name='section',
        ),
        migrations.RemoveField(
            model_name='studentclass',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentsection',
            name='section',
        ),
        migrations.RemoveField(
            model_name='studentsection',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentsubject',
            name='kgsubject',
        ),
        migrations.RemoveField(
            model_name='studentsubject',
            name='level',
        ),
        migrations.RemoveField(
            model_name='studentsubject',
            name='midsubject',
        ),
        migrations.RemoveField(
            model_name='studentsubject',
            name='prsubject',
        ),
        migrations.RemoveField(
            model_name='studentsubject',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentassignment',
            name='Section',
        ),
        migrations.RemoveField(
            model_name='studentassignment',
            name='kgclass',
        ),
        migrations.RemoveField(
            model_name='studentassignment',
            name='kgsubject',
        ),
        migrations.RemoveField(
            model_name='studentassignment',
            name='midclass',
        ),
        migrations.RemoveField(
            model_name='studentassignment',
            name='midsubject',
        ),
        migrations.RemoveField(
            model_name='studentassignment',
            name='prclass',
        ),
        migrations.RemoveField(
            model_name='studentassignment',
            name='prsubject',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentClass',
        ),
        migrations.DeleteModel(
            name='StudentSection',
        ),
        migrations.DeleteModel(
            name='StudentSubject',
        ),
        migrations.AddField(
            model_name='studentassignment',
            name='sectionsubject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='StudentSectionClassSubject01', to='Beezaccs.studentsectionclasssubject'),
        ),
    ]