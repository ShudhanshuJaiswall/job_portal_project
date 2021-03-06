# Generated by Django 3.2.9 on 2021-12-01 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_jobdettails'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdettails',
            name='company_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobdettails',
            name='logo',
            field=models.ImageField(default='', upload_to='app/img/jobpost'),
        ),
    ]
