# Generated by Django 3.1.3 on 2020-11-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprestapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
