# Generated by Django 3.0.2 on 2020-01-16 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('pmp_code', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=11)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employerR.Position')),
            ],
        ),
    ]
