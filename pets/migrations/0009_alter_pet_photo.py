# Generated by Django 3.2 on 2021-04-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_alter_pet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(null=True, upload_to='uploads/photos/', verbose_name='Фото'),
        ),
    ]
