# Generated by Django 4.2.7 on 2023-12-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBehavior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('user_name', models.CharField(max_length=100)),
                ('behavior', models.CharField(max_length=100)),
            ],
        ),
    ]
