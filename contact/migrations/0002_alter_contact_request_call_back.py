# Generated by Django 3.2 on 2022-07-11 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='request_call_back',
            field=models.CharField(
                choices=[
                    ('NO_REQUEST_CALL_BACK',
                     'No'),
                    ('REQUEST_CALL_BACK',
                     'Yes')],
                max_length=20),
        ),
    ]
