# Generated by Django 4.0.2 on 2022-02-16 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_5', '0002_auto_20200517_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
