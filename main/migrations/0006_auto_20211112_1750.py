# Generated by Django 3.2.7 on 2021-11-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_tomeet_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='comment',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='habits',
            name='done_for_today',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='habits',
            name='important',
            field=models.CharField(max_length=300),
        ),
    ]