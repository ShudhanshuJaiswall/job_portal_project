# Generated by Django 3.2.9 on 2021-12-03 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20211201_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppltList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('min_salary', models.CharField(max_length=100)),
                ('max_salary', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('resume', models.FileField(upload_to='app/resume')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jobdettails')),
            ],
        ),
    ]
