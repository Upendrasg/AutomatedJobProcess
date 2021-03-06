# Generated by Django 2.0 on 2019-03-12 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_apply', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Applyed_application', to='job_apply.User')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Applyed_vacancy', to='job_apply.Vacancy')),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='work_experience_ends',
            field=models.DateField(verbose_name='End Data'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='work_experience_starts',
            field=models.DateField(verbose_name='End Data'),
        ),
        migrations.AlterField(
            model_name='training',
            name='training_ends',
            field=models.DateField(verbose_name='End Data'),
        ),
        migrations.AlterField(
            model_name='training',
            name='training_starts',
            field=models.DateField(verbose_name='Start Date'),
        ),
    ]
