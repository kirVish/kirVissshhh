# Generated by Django 3.2 on 2021-04-20 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['-date_posted']},
        ),
    ]