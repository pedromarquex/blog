# Generated by Django 2.2.1 on 2019-05-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190521_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lead',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]