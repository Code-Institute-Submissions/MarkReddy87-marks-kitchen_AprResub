# Generated by Django 3.2 on 2022-04-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, default='placeholder', upload_to='images/'),
        ),
    ]
