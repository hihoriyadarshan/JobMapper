# Generated by Django 4.1.5 on 2023-04-11 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_catagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='category_description',
        ),
    ]